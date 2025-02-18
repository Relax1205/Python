import math


def calculate_term(c, y, j):
    term1 = 45 * (c ** 3 + y + 34) ** 7
    term2 = (j ** 2) / 23
    term3 = 31 * math.cos(1 + j ** 3) ** 4
    return term1 + term2 + term3


def main(a, b, y):
    total = 0
    j = 1
    while j <= b:
        c = 1
        while c <= a:
            total += calculate_term(c, y, j)
            c += 1
        j += 1
    return total


print(main(7, 8, -0.24))
print(main(3, 5, 0.71))
