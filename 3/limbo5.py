import math

def main(a, b, y):
    def calculate_term(c, j):
        term1 = 45 * ((c**3 + y + 34) ** 7)
        term2 = (j**2) / 23
        term3 = 31 * (math.cos(1 + j**3) ** 4)
        return term1 + term2 + term3

    result = 0
    for j in range(1, b + 1):
        for c in range(1, a + 1):
            result += calculate_term(c, j)

    return result



print(main(7, 8, -0.24))
print(main(3, 5, 0.71))