import argparse
import enum

class Color(enum.Enum):
    white = 'white'
    RG = 'rg'
    all = 'all'

    def __str__(self):
        return self.value
    
def integer_type(num, type, str, min, max=None):
    try:
        num = type(num)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Must be a {type}.")
    if num < min or num > max if max else False:
        raise argparse.ArgumentTypeError(str)
    return num

def positive_float(arg):
    return integer_type(arg, float, "Argument must be a positive float", 0)

def percentage(arg):
    return integer_type(arg, int, "Argument must be a number between 0 and 100.", 0, 100)