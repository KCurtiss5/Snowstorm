import argparse

colors = {
    'rg': ['\033[91m', '\033[92m'],  # bright red, bright green
    'all': [
        '\033[31m', '\033[32m',  # red, green
        '\033[33m', '\033[34m',  # yellow & blue
        '\033[35m', '\033[36m',  # magenta & cyan
        '\033[37m',              # white
        '\033[90m', '\033[91m',  # dark grey (bright black) & bright red
        '\033[92m', '\033[93m',  # bright green & bright yellow
        '\033[94m', '\033[95m',  # bright blue & bright magenta
        '\033[96m', '\033[97m',  # bright cyan & bright white
        # Add more colors as needed
    ]
}


def my_type(num, type, min, max=None):
    try:
        num = type(num)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Must be a {type}.")
    if num < min or num > max if max else False:
        raise argparse.ArgumentTypeError(
            f"Argument must be a {type} between {min} and {max}")
    return num


def positive_float(arg):
    return my_type(arg, float, 0, 10)


def percentage(arg):
    return my_type(arg, int, 0, 100)
