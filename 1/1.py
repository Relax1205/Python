import math


def main(x, y, z):
    numerator = (82 * z**3 + 21 * y**2)**4 + (x - 23 * z**3 - y**2 / 6)**3
    denominator = (59 * y**2 + 85 * z**3 + x / 98)**2
    first_term = math.sqrt(numerator / denominator)

    second_term_numerator = 12 * (53 * y + 9 * z**3 + x**2)**7 + 40 * x**3
    second_term_denominator = 86 * y**2 - (z**2 + 56 + 71 * x**3)**6 / 16
    second_term = second_term_numerator / second_term_denominator

    return first_term + second_term
    
print(main(0.09, -0.3, -0.21))
print(main(0.75, 0.29, -0.76))