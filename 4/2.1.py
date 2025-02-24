import math


def main(n):
    if n == 0:
        return 0.89
    
    prev_value = 0.89
    for i in range(1, n + 1):
        current_value = 93 + math.log(prev_value) ** 3 + prev_value
        prev_value = current_value
    
    return current_value

print(main(1))
print(main(2))
print(main(6))