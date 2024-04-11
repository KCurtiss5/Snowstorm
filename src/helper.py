def clamp(n, minimum, maximum):
    return (max(minimum, min(n, maximum)))


def count_new_snowflakes(width, new_row):
    return width - list.count(new_row, ' ')

def count_snowflakes(width, grid):
    total = 0
    for line in grid:
        total += width - list.count(line, ' ')
    return total
