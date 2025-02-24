def compute_f(n):
    if n == 0:
        return 0.07
    elif n == 1:
        return 0.24
    else:
        f_n_minus_1 = compute_f(n-1)
        f_n_minus_2 = compute_f(n-2)
        return 65 - (f_n_minus_1 - f_n_minus_2 ** 2) / 55