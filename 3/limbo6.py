import math


def calculate_term(c, j, y):
    term1 = 45 * ((c**3 + y + 34) ** 7)
    term2 = (j**2) / 23
    term3 = 31 * (math.cos(1 + j**3) ** 4)
    return term1 + term2 + term3


def main(a, b, y):
    def calculate_for_j(j):
        return sum(calculate_term(c, j, y) for c in range(1, a + 1))

    return sum(map(calculate_for_j, range(1, b + 1)))

print(main(7, 8, -0.24))
print(main(3, 5, 0.71))