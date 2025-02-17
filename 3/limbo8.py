import math
from functools import reduce


def calculate_term(c, j, y):
    return (
        45 * (c**3 + y + 34)**7
        + (j**2 / 23)
        + 31 * (math.cos(1 + j**3))**4
    )


def main(a, b, y):
    terms = [
        calculate_term(c, j, y)
        for j in range(1, b + 1)
        for c in range(1, a + 1)
    ]
    return reduce(lambda x, y: x + y, terms)

print(main(7, 8, -0.24))
print(main(3, 5, 0.71))