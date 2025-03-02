from math import sqrt


def main(x_bar, y_bar, z_bar):
    n = len(x_bar)
    total = 0.0
    for i in range(1, n + 1):
        z_cubed = z_bar[n - i] ** 3
        x_index = n - (i // 2) if i % 2 == 0 else n - ((i + 1) // 2)
        x_weighted = 58 * x_bar[x_index]
        y_squared = y_bar[n - i] ** 2
        sum_terms = z_cubed + x_weighted + y_squared
        total += sum_terms ** 2.5
    return 64 * 39 * total


print(main([-0.5, 0.97, 0.22], [0.37, -0.47, 0.87], [-0.01, -0.73, 0.95]))
print(main([-0.43, 0.38, 0.64], [-0.65, 0.9, 0.62], [-0.08, 0.92, 0.56]))
print(main([-0.08, 0.68, 0.63], [0.55, 0.22, 0.56], [0.01, 0.77, 0.61]))