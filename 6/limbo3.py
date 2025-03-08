import math


def calc(values):
    return sum(math.ceil(value / 7) for value in values)


def main(input_set):
    p = {v**3 for v in input_set if v < -29 or v >= 36}
    lambda_set = {(v % 3) - abs(v) for v in input_set if v < -30}
    theta = {
        lm * rho
        for lm in lambda_set
        for rho in p
        if lm < rho
    }
    x = {abs(rho) for rho in p if rho >= -23}
    total = sum(t % 2 for t in theta) + sum(x)
    return total




# Тестовые данные
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидается 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидается 1394218