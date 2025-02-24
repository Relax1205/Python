import math


def main(n):
    match n:
        case 0:
            return 0.89
        case _:
            prev = main(n - 1)
            return 93 + math.log(prev) ** 3 + prev

print(main(1))  # Вывод: -0.38
print(main(2))  # Вывод: значение f(2)
print(main(6))