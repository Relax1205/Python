import math


def main(n):
    values = [0.89]
    for i in range(1, n + 1):
        prev_value = values[i - 1]
        new_value = 93 + math.log(prev_value) ** 3 + prev_value
        values.append(new_value)
    return values[n]


print(main(1))
print(main(2))
print(main(6))