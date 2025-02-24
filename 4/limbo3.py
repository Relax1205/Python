import math


def main(n):
    value1 = 0.07
    value2 = 0.24
    for i in range(2, n + 1):
        value1, value2 = 65 - (value1 - value2 ** 2) / 55, value1
    return value1

print(main(3))