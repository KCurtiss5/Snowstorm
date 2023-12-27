import argparse
from enum import Enum

class Color(Enum):
    white = 'white'
    RG = 'rg'
    all = 'all'

    def __str__(self):
        return self.value

def do_parsing():
    parser = argparse.ArgumentParser(
        prog='Snowstorm',
        description='snowstorm - create a local snowstorm in your terminal',
        #epilog='Example\npython snowstorm.py -c RG -w')
    )
    parser.add_argument('-c', '--color', type=Color, choices=list(Color), default="white", 
                    help='Set the color of snowflakes to white, red & green or a random color.')
    parser.add_argument('-w', '--wind', action='store_true',
                    help='Enable wind. The wind direction is random and can change in runtime.')
    parser.add_argument('-a', '--accumulate', nargs='?', default=0, const=5, type=int, choices=range(0, 101), metavar='NUM',
                    help='Snowflakes have a NUM percentage chance to result in a █ character and "accumulate" at the bottom.')
    args = parser.parse_args()
    return (args.color, args.wind, args.accumulate)

if __name__ == "__main__":
    color, wind, accumulate = do_parsing()
    print(wind)
