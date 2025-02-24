import math


def main(n):
    if n == 0:
        return 0.89
    a = 0.89
    count = 0
    while count < n:
        a = 93 + math.log(a) ** 3 + a
        count += 1
    return a


print(main(1))
print(main(2))
print(main(6))