from math import log, exp


def main(x_bar, y_bar, z_bar):
    n = len(x_bar)
    summa = 0.0
    for i in range(1, n + 1):
        step1 = z_bar[n - i]**3
        if i % 2 == 0:
            step2 = 58 * x_bar[n - (i // 2)]
        else:
            step2 = 58 * x_bar[n - ((i + 1) // 2)]
        step3 = y_bar[n - i]**2
        a = step1 + step2 + step3
        term = exp((5/2) * log(a))
        summa += term
    return 64 * 39 * summa


print(main([-0.5, 0.97, 0.22], [0.37, -0.47, 0.87], [-0.01, -0.73, 0.95]))  # ≈ 6.30e+07
print(main([-0.43, 0.38, 0.64], [-0.65, 0.9, 0.62], [-0.08, 0.92, 0.56]))  # ≈ 5.10e+07
print(main([-0.08, 0.68, 0.63], [0.55, 0.22, 0.56], [0.01, 0.77, 0.61]))  # ≈ 6.66e+07