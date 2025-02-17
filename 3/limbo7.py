import math


def main(a, b, y):
    def generator():
        for j in range(1, b + 1):
            for c in range(1, a + 1):
                term1 = 45 * ((c**3 + y + 34) ** 7)
                term2 = (j**2) / 23
                term3 = 31 * (math.cos(1 + j**3) ** 4)
                yield term1 + term2 + term3

    return sum(generator())

print(main(7, 8, -0.24))
print(main(3, 5, 0.71))