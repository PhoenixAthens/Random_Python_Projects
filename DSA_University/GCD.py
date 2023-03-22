import math


def GCD(num1, num2):
    if first % second == 0:
        return second
    elif second % first == 0:
        return first
    else:
        answer = 1
        divisor = 2
        while (divisor <= first) and (divisor <= second):
            if first % divisor == 0 and second % divisor == 0:
                answer = divisor
            divisor += 1
        return answer


first = eval(input("Enter the first number: "))
second = eval(input("Enter the second number: "))
print("The GCD of our values is " + str(GCD(first, second)))
print("In-built function: " + str(math.gcd(first, second)))

