import math


def main(x, y, z):
    numerator_part1 = math.pow(
        82 * math.pow(z, 3) + 21 * math.pow(y, 2), 4
    )
    numerator_part2 = math.pow(
        x - 23 * math.pow(z, 3) - math.pow(y, 2) / 6, 3
    )
    denominator_part1 = math.pow(
        59 * math.pow(y, 2) + 85 * math.pow(z, 3) + x / 98, 2
    )

    sqrt_expression = math.sqrt(
        (numerator_part1 + numerator_part2) / denominator_part1
    )

    numerator_part3 = 12 * math.pow(
        53 * y + 9 * math.pow(z, 3) + math.pow(x, 2), 7
    )
    numerator_part4 = 40 * math.pow(x, 3)
    denominator_part2 = (
        86 * math.pow(y, 2) -
        math.pow(math.pow(z, 2) + 56 + 71 * math.pow(x, 3), 6) / 16
    )

    fraction_expression = (
        (numerator_part3 + numerator_part4) / denominator_part2
    )

    return sqrt_expression + fraction_expression


print(main(0.09, -0.3, -0.21))
print(main(0.75, 0.29, -0.76))