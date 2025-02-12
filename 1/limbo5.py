import math


def calculate_numerator_first_term(z, y):
    return (82 * z**3 + 21 * y**2)**4


def calculate_additional_term_first_term(x, z, y):
    return (x - 23 * z**3 - y**2 / 6)**3


def calculate_denominator_first_term(y, z, x):
    return (59 * y**2 + 85 * z**3 + x / 98)**2


def calculate_first_term(x, y, z):
    numerator = (
        calculate_numerator_first_term(z, y) +
        calculate_additional_term_first_term(x, z, y))
    denominator = calculate_denominator_first_term(y, z, x)
    return math.sqrt(numerator / denominator)


def calculate_numerator_second_term(y, z, x):
    return (
        12 * (53 * y + 9 * z**3 + x**2)**7 +
        40 * x**3
    )


def calculate_denominator_second_term(y, z, x):
    return (
        86 * y**2 -
        (z**2 + 56 + 71 * x**3)**6 / 16
    )


def calculate_second_term(x, y, z):
    numerator = calculate_numerator_second_term(y, z, x)
    denominator = calculate_denominator_second_term(y, z, x)
    return numerator / denominator


def main(x, y, z):
    first_term = calculate_first_term(x, y, z)
    second_term = calculate_second_term(x, y, z)
    return first_term + second_term


print(main(0.09, -0.3, -0.21))
print(main(0.75, 0.29, -0.76))