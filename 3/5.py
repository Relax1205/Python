import math


def calculate_term(c, j, y):
    term1 = 45 * ((c**3 + y + 34) ** 7)
    term2 = (j**2) / 23
    term3 = 31 * (math.cos(1 + j**3) ** 4)
    return term1 + term2 + term3


def main(a, b, y, c=1, j=1, result=0):
    if j > b:
        return result
    if c > a:
        return main(a, b, y, 1, j + 1, result)
    return main(a, b, y, c + 1, j, result + calculate_term(c, j, y))


print(main(7, 8, -0.24))
print(main(3, 5, 0.71))
