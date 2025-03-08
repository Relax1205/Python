def compute_p(upsilon):
    return [v**3 for v in upsilon if v < -29 or v >= 36]


def compute_lambda(upsilon):
    return [(v % 3) - abs(v) for v in upsilon if v < -30]


def compute_theta(lambda_, p):
    theta = []
    for lambda_val in lambda_:
        for rho in p:
            if lambda_val < rho:
                theta.append(lambda_val * rho)
    return theta


def compute_x(p):
    return [abs(rho) for rho in p if rho >= -23]


def main(upsilon):
    p = compute_p(upsilon)
    lambda_ = compute_lambda(upsilon)
    theta = compute_theta(lambda_, p)
    x = compute_x(p)
    odd_theta_count = sum(1 for val in theta if val % 2 != 0)
    return odd_theta_count + sum(x)



print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))
