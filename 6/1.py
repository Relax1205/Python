def main(A):
    Phi = {abs(alpha) for alpha in A if alpha < -47 or alpha > -29}
    Z = A.union(Phi)
    T = {phi * zeta for phi in Phi for zeta in Z if phi >= zeta}
    v = len(Z) - sum(8 * tau for tau in T)
    return v


# Примеры вызова функции
print(main({4, -28, -82, -46, 87, -41, 56, 94, 95}))  # Ожидаемый результат: 2522078
print(main({-30, -93, 5, 40, -20, -50, 81, 83, 61, -98}))  # Ожидаемый результат: 1394218