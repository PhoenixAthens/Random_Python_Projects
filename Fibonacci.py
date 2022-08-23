def fib(n):
    if n == 1 or n == 2:
        return 1
    num1 = fib(n-1)
    num2 = fib(n-2)
    return num1+num2

number = fib(37)

print(number)