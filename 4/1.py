import math


def main(n):
    if n == 0:
        return 0.89
    else:
        prev = main(n - 1)
        return 93 + math.log(prev) ** 3 + prev


print(main(1))
print(main(2))
print(main(6))