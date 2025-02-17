import math


def main(a, b, y):
    return sum(
        45 * ((c**3 + y + 34) ** 7) + (j**2) / 23 + 31 * (math.cos(1 + j**3) ** 4)
        for j in range(1, b + 1)
        for c in range(1, a + 1)
    )


print(main(7, 8, -0.24))
print(main(3, 5, 0.71))