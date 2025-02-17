import math


def calculate_term(c, j, y):
    return (
        45 * (c**3 + y + 34)**7
        + (j**2 / 23)
        + 31 * (math.cos(1 + j**3))**4
    )


def main(a, b, y, j=1, c=1, total=0):
    if j > b:
        return total
    if c > a:
        return main(a, b, y, j + 1, 1, total)
    term = calculate_term(c, j, y)
    return main(a, b, y, j, c + 1, total + term)

print(main(7, 8, -0.24))
print(main(3, 5, 0.71))