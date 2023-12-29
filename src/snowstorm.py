import argparse
import os
import random
import time
from custom_types import percentage, positive_float, colors
from helper import clamp


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Snowstorm',
        description='snowstorm - create a local snowstorm in your terminal',
    )
    parser.add_argument('-d', '--density', default=5, type=percentage,
        help='Set the percentage of the screen to be snowflakes. Default: 5')
    parser.add_argument('-t', '--delay', default=.3, type=positive_float,
        help='Set the delay in seconds before spawning new snowflakes and moving others to DELAY. Default: 0.3')
    parser.add_argument('-c', '--color', type=str, choices=["white", "rg", "all"], default="white",
        help='Set the color of snowflakes to white, red & green, or a random color. Default: white')
    parser.add_argument('-w', '--wind', action='store_true',
        help='Enable wind. The wind direction is random and can change in runtime. Defailt: False')
    parser.add_argument('-a', '--accumulate', nargs='?', default=False, const=5, type=percentage,
        help='Snowflakes have a NUM percentage chance to result in a █ character and "accumulate" at the bottom. Default: False, or 5 if enabled.')
    args = parser.parse_args()
    return (args.density, args.delay, args.color, args.wind, args.accumulate)


def draw_snowflakes(grid, height):
    output = ''
    for row in grid:
        output += row + '\n'
    output = output.strip('\n')
    print(output, end='')
    print('\033[F' * height, end='')


def add_snowflake(density, color):
    snowflakes = ['❅', '❆', '❃', '❈', '❉', '*', '•', '·']
    if random.random() < density/100:
        snowflake = random.choice(snowflakes)
        if (color != "white"):
            snowflake = add_color(snowflake, color)
        return snowflake
    else:
        return ' '


def add_color(snowflake, color):
    RESET = '\033[0m'
    color = random.choice(colors[color])
    return color + snowflake + RESET


def add_wind(grid, strength, num_rows, density, color):
    if strength > 0:
        for i in range(min(len(grid), num_rows)):
            grid[i] = ''.join(add_snowflake(density, color) for _ in range(strength)) + grid[i][:-strength]
    elif strength < 0:
        strength = abs(strength)
        for i in range(min(len(grid), num_rows)):
            grid[i] = grid[i][strength:] + ''.join(add_snowflake(density, color) for _ in range(strength))


def main():
    density, delay, color, wind, accumulate = parse_arguments()
    width, height = os.get_terminal_size()

    wind_strength = random.randint(-3, 3)
    rows_with_snow = 0

    grid = [' ' * width] * height

    while True:
        row = ''

        for _ in range(width):
            row += add_snowflake(density, color)
        rows_with_snow += 1
        rows_with_snow = clamp(rows_with_snow, 0, height)

        if (wind):
            wind_strength += random.randint(-1, 1)
            wind_strength = clamp(wind_strength, -3, 3)
            add_wind(grid, wind_strength, rows_with_snow, density, color)

        grid.insert(0, row)
        grid.pop()
        draw_snowflakes(grid, height)

        time.sleep(delay)


if __name__ == "__main__":
    main()
