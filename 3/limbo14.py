import math

def main(a, b, y):
    matrix = []
    for j in range(1, b + 1):
        row = []
        for c in range(1, a + 1):
            term = (
                45 * ((c**3 + y + 34) ** 7)
                + (j**2 / 23)
                + 31 * (math.cos(1 + j**3) ** 4)
            )
            row.append(term)
        matrix.append(row)
    return sum(sum(row) for row in matrix)

print(main(7, 8, -0.24))
print(main(3, 5, 0.71))