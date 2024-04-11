def clamp(n, minimum, maximum):
    return (max(minimum, min(n, maximum)))


def count_snowflakes(width, row):
    return width - list.count(row, ' ')

def count_total_snowflakes(width, grid):
    total = 0
    for row in grid:
        total += count_snowflakes(width, row)
    return total

def init_grid(height, width) -> list:
    return [[' ' for _ in range(width)] for _ in range(height)]
