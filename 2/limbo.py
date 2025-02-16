from math import *


def main(x):
    if x < 117:
        return 702 * x + 61 * (75 * x + 1 + x**3)**5
    elif 117 <= x < 143:
        tan_value = tan(x + 75 * x**2 + 1)
        return tan_value**6 - 49 * x**7 - 68 * x**2
    elif 143 <= x < 195:
        return 48 * (log(x))**6
    else:
        term1 = 86 * x**6
        term2 = (37 * x - 55 * x**3 - 99 * x**2)**2
        term3 = 62 * (37 + x**2 / 31 + 8 * x**3)**5
        return term1 - term2 - term3
    
print(main(43))  
print(main(49))
print(main(141))
print(main(83))