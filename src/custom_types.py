from argparse import ArgumentTypeError


def positive(arg):
    num = float(arg)
    if num <= 0:
        raise ArgumentTypeError("Delay must be positive.")
    return num


def percentage(arg):
    num = int(arg)
    if num < 0 or num > 100:
        raise ArgumentTypeError("Argument must be an int between 0 and 100.")
    return num
