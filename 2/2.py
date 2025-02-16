import math


def main(x):
    return (
        702 * x + 61 * (75 * x + 1 + x**3)**5 if x < 117 else
        math.tan(x + 75 * x**2 + 1)**6 - 49 * x**7 - 68 * x**2
        if 117 <= x < 143 else
        48 * (math.log(x))**6 if 143 <= x < 195 else
        86 * x**6 - (37 * x - 55 * x**3 - 99 * x**2)**2 -
        62 * (37 + x**2 / 31 + 8 * x**3)**5
    )

print(main(43))  
print(main(49))
print(main(141))
print(main(83))