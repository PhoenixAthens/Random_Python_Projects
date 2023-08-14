def powerOfFactor(num, fact):
    if num == fact:
        return 1
    elif num%fact == 0:
        return powerOfFactor(num//fact,fact)+1
    return 0


"""
print(powerOfFactor(1024,2)) # 10
print(powerOfFactor(8,8)) # 1
print(powerOfFactor(10,3)) # 0
"""

# testing in a separate file (testCoverage.py)