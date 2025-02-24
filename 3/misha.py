import math


def calculate_term(i, k, j):
    term = 27 * (abs(i**2 + k + 54 * j**3))**2
    return term


def main(b, a, n, i=1, k=1, j=1, result=0):
    if j > n:
        return result
    if k > a:
        return main(b, a, n, 1, 1, j + 1, result)
    if i > b:
        return main(b, a, n, 1, k + 1, j, result)
    return main(b, a, n, i + 1, k, j, result + calculate_term(i, k, j))


print(main(2, 2, 7))  # Замените значения на нужные
print(main(6, 3, 2))  # Замените значения на нужные