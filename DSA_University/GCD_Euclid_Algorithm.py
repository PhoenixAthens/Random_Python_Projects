import math


def GCD_calculator(num1: int, num2: int):
    if num2 == 0:
        return num1
    res: int = num1 % num2
    return GCD_calculator(num2, res)


val1: int = eval(input("Enter the first number: "))
val2: int = eval(input("Enter the second number: "))
GCD: int
value1_abs: int = abs(val1)
value2_abs: int = abs(val2)
if value1_abs == value2_abs:
    GCD = value1_abs
elif value1_abs > value2_abs:
    GCD = GCD_calculator(value1_abs, value2_abs)
else:
    GCD = GCD_calculator(value2_abs, value1_abs)
print(f"The GCD of {val1} and {val2} is {GCD}")