def MaxMin(x, y, z):
    maximum = max(x, y, z)
    minimum = min(x, y, z)
    return maximum, minimum


x, y = MaxMin(eval(input("Enter first number: ")), eval(input("Enter second number: ")),
              eval(input("Enter third number: ")))
print(f"Maximum: {x}; Minimum: {y}")
