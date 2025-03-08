import math


def calc(values):
    return sum(math.ceil(val / 7) for val in values)


def main(input_data):
    # Формирование множества P
    p = [v**3 for v in input_data if v < -29 or v >= 36]
    # Формирование lambda_set
    lambda_set = [(v % 3) - abs(v) for v in input_data if v < -30]
    # Вычисление theta с использованием генератора
    theta = (lm * rho for lm in lambda_set for rho in p if lm < rho)
    # Формирование множества X
    x = [abs(rho) for rho in p if rho >= -23]
    return sum(t % 2 for t in theta) + sum(x)


# Тестовые данные
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидается 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидается 1394218

