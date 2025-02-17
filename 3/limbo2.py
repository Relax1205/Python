import math
from functools import lru_cache


@lru_cache(None)
def calculate_term(c, j, y):
    term1 = 45 * (c**3 + y + 34)**7
    term2 = j**2 / 23
    term3 = 31 * (math.cos(1 + j**3))**4
    return term1 + term2 + term3


def main(a, b, y):
    return sum(
        calculate_term(c, j, y)
        for j in range(1, b + 1)
        for c in range(1, a + 1)
    )


print(main(7, 8, -0.24))
print(main(3, 5, 0.71))