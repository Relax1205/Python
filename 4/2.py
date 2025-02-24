import math


def main(n):
    a = 0.89
    for _ in range(n):
        a = 93 + math.log(a) ** 3 + a
    return a

print(main(1))
print(main(2))
print(main(6))