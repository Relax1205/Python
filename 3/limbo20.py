import math
from functools import reduce
from itertools import product


def calculate_term(c, j, y):
    return (
        45 * ((c**3 + y + 34) ** 7) +
        (j**2) / 23 +
        31 * (math.cos(1 + j**3) ** 4)
    )


def main(a, b, y):
    return reduce(
        lambda acc, pair: acc + calculate_term(pair[0], pair[1], y),
        product(range(1, a + 1), range(1, b + 1)),
        0
    )


print(main(7, 8, -0.24))
print(main(3, 5, 0.71))
