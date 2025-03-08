import math
from itertools import product


def calc(values):
    return sum(math.ceil(v / 7) for v in values)


def compute_p(data):
    return (v ** 3 for v in data if v < -29 or v >= 36)


def compute_lambda(data):
    return ((v % 3) - abs(v) for v in data if v < -30)


def compute_theta(lambda_vals, p_vals):
    return (l_val * p_val for l_val, p_val in product(lambda_vals, p_vals) 
            if l_val < p_val)


def compute_x(p_vals):
    return (abs(p) for p in p_vals if p >= -23)


def main(input_set):
    p_values = list(compute_p(input_set))
    lambda_values = list(compute_lambda(input_set))
    theta_values = compute_theta(lambda_values, p_values)
    x_values = compute_x(p_values)
    return sum(t % 2 for t in theta_values) + sum(x_values)


# Тестовые данные
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидается 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидается 