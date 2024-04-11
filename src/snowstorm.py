import argparse
import os
import random
import time
import math
from custom_types import percentage, positive
from colors import COLORS
from helper import clamp, count_new_snowflakes, count_snowflakes

#constants
RESET = '\033[0m'
SNOWFLAKES = ['❅', '❆', '❃', '❈', '❉', '*', '•', '·']
START_TIME = time.time()

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Snowstorm',
        description='snowstorm - create a snowstorm in your terminal',
    )
    parser.add_argument('-d', '--density', default=5, type=percentage,
        help='Set the percentage of the screen to be snWowflakes. Default: 5')
    parser.add_argument('-t', '--delay', default=.3, type=positive,
        help='Set the delay in seconds before snowflakes fall. Default: 0.3')
    parser.add_argument('-c', '--color', type=str, choices=["white", "rg", "all"], default="white",
        help='Set the color of snowflakes to white, red & green, or a random color. Default: white')
    parser.add_argument('-w', '--wind', action='store_true',
        help='Enable wind. The wind direction is random and can change in runtime. Defailt: False')
    parser.add_argument('-a', '--accumulate', nargs='?', default=False, const=5, type=percentage,
        help='Snowflakes have a NUM percent chance to accumulate. Default: False or 5')
    parser.add_argument('-v', '--statistics', action='store_true',
        help='Enable program statistics. Default = False')
    args = parser.parse_args()
    return (args.density, args.delay, args.color,
            args.wind, args.accumulate, args.statistics)


def draw_snowflakes(grid, height, stats_str=None):
    output = '\n'.join(''.join(row) for row in grid)
    print(output, end='')
    if stats_str:
        print(stats_str, end='\033[F')
    print('\033[F' * height, end='')


def add_snowflake(density, color):
    return add_color(random.choice(SNOWFLAKES), color) if random.random() < density/100 else ' '


def add_color(snowflake, color):
    color = random.choice(COLORS[color])
    return color + snowflake + RESET

def make_stats_str(width, tot_snowflakes, cur_snowflakes, num_frames, runtime) -> str:
    tot_snow = f"Total Snowflakes: {tot_snowflakes}"
    cur_snow = f"Current Snowflakes: {cur_snowflakes}"
    frames = f"Total Frames: {num_frames}"
    time_str = f"Runtime: {runtime} seconds"

    # Calculate available space for aligning components
    total_length = sum(map(len, [tot_snow, cur_snow, frames, time_str]))
    available_space = width - total_length
    spaces, extra = ' ' * (available_space//3), ' ' * (available_space % 3)

    return tot_snow + spaces + cur_snow + spaces + frames + spaces + time_str + extra


def add_wind(grid, strength, num_rows, density, color):
    if strength == 0:
        return
    rightward = strength > 0
    strength = abs(strength)

    for i in range(min(len(grid), num_rows)):
        snowflakes = [''.join(add_snowflake(density, color) for _ in range(strength))]
        if rightward:
            grid[i] = snowflakes + grid[i][:-strength]
        else:
            grid[i] = grid[i][strength:] + snowflakes

def main():
    density, delay, color, wind, accumulate, stats = parse_arguments()
    width, height = os.get_terminal_size()

    if stats:
        height -= 1

    wind_strength = random.randint(-3, 3)
    rows_with_snow = 0

    #stats variables
    total_snowflakes = 0
    stats_str = None
    num_frames = 0

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    while True:
        row = []

        for _ in range(width):
            row.append(add_snowflake(density, color))

        rows_with_snow += 1
        rows_with_snow = clamp(rows_with_snow, 0, height)
        if stats:
            total_snowflakes += count_new_snowflakes(width, row)
            stats_str = make_stats_str(
                width, total_snowflakes, count_snowflakes(width, grid), num_frames,
                math.floor(time.time() - START_TIME))

        if wind:
            wind_strength += random.randint(-1, 1)
            wind_strength = clamp(wind_strength, -3, 3)
            add_wind(grid, wind_strength, rows_with_snow, density, color)

        if accumulate:
            pass #to get pylint to pass for now

        grid.insert(0, row)
        grid.pop()
        draw_snowflakes(grid, height, stats_str)

        num_frames += 1
        time.sleep(delay)


if __name__ == "__main__":
    main()
