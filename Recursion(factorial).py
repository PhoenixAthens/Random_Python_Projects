flag = True


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


while flag:

    num = int(input("Enter a number"))
    result = factorial(num)
    print(f"Factorial of {num}: " + str(result))
    reply = int(input("To repeat hit 1"))
    if reply != 1:
        flag = False
