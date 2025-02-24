def main(n):
    return (
        0.19 if n == 0 else
        -0.38 if n == 1 else
        (lambda x, y: x + (y / 16) ** 3 + 47 * y ** 2)(main(n - 1), main(n - 2))
    )

print(main(1))
print(main(2))
print(main(6))