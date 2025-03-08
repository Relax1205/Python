import math


def calc(i):
    return sum(math.ceil(alph / 7) for alph in i)


def main(input_set):
    P = {v ** 3 for v in input_set if v < -29 or v >= 36}
    Lambda = {(v % 3) - abs(v) for v in input_set if v < -30}
    Theta = {lambda_val * rho for lambda_val in Lambda 
             for rho in P if lambda_val < rho}
    X = {abs(rho) for rho in P if rho >= -23}
    sum_theta_mod = sum(t % 2 for t in Theta)
    sum_x = sum(X)
    return sum_theta_mod + sum_x

# Тестовые данные
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидается 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидается 1394218