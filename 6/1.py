def main(upsilon):
    p = [v**3 for v in upsilon if v < -29 or v >= 36]
    lambda_ = [(v % 3) - abs(v) for v in upsilon if v < -30]
    theta = [
        lambda_val * rho
        for lambda_val in lambda_
        for rho in p
        if lambda_val < rho
    ]
    x = [abs(rho) for rho in p if rho >= -23]
    return sum(theta_val % 2 for theta_val in theta) + sum(x)

# Примеры вызова функции
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидаемый результат: 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидаемый результат: 1394218