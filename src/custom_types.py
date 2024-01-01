from argparse import ArgumentTypeError


def _my_type(num, type, min, max=None):
    try:
        num = type(num)
    except ValueError:
        raise ArgumentTypeError(f"Must be a {type}.")
    if num < min or num > max if max else False:
        raise ArgumentTypeError(
            f"Argument must be a {type} between {min} and {max}")
    return num


def positive_float(arg):
    return _my_type(arg, float, 0, 10)


def percentage(arg):
    return _my_type(arg, int, 0, 100)
