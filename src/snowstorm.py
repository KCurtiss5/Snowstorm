import argparse
import os
import random
import time
from custom_types import percentage, positive_float, Color


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Snowstorm',
        description='snowstorm - create a local snowstorm in your terminal',
    )
    parser.add_argument('-d', '--density', default=5, type=percentage,
        help='Set the percentage of the screen to be snowflakes. Default: 5')
    parser.add_argument('-t', '--delay', default=.3, type=positive_float,
        help='Set the delay in seconds before spawning new snowflakes and moving others to DELAY. Default: 0.3')
    parser.add_argument('-c', '--color', type=Color, choices=list(Color), default="white",
        help='Set the color of snowflakes to white, red & green or a random color. Default: white')
    parser.add_argument('-w', '--wind', action='store_true',
        help='Enable wind. The wind direction is random and can change in runtime. Defailt: False')
    parser.add_argument('-a', '--accumulate', nargs='?', default=False, const=5, type=percentage,
        help='Snowflakes have a NUM percentage chance to result in a █ character and "accumulate" at the bottom. Default: False, or 5 if enabled.')
    args = parser.parse_args()
    return (args.density, args.delay, args.color, args.wind, args.accumulate)


def draw_grid(grid, height):
    output = ''
    for row in grid:
        output += ''.join(row) + '\n'
    output = output.strip('\n')
    print(output, end='')
    print('\033[F' * height, end='')


def main():
    density, delay, color, wind, accumulate = parse_arguments()
    snowflakes = ['❅', '❆', '❃', '❈', '❉', '*', '•', '·']
    width, height = os.get_terminal_size()

    grid = [' ' * width] * height

    while True:
        row = []

        for _ in range(width):
            if random.random() < density/100:
                row.append(random.choice(snowflakes))
            else:
                row.append(' ')

        grid.insert(0, row)
        grid.pop()
        draw_grid(grid, height)

        time.sleep(delay)


if __name__ == "__main__":
    main()
