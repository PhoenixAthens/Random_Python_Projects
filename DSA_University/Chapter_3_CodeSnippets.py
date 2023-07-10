import math
# while-loop
n : int = 1
while n<=25:
    print(n)
    n+=1

# for loop
values:[int] = [1,2,3,4,5,6,7,8,9,10]
for val in values:
    print(val)

# for with else
"""
The else part is optional and 
executed when the for loop exits normally. 
It will not execute when the exit is through a break statement.
"""

for val in values:
    print(f"Printing: {val}")
else:
    print("Iteration completed!!")

# using range(i,j) (i-inclusive & j-exclusive)
listOfValues = range(1,10)
for i in listOfValues:
    print(i)

for i in range(0,101,2):
    if i % 3 == 0 and i % 5 ==0:
        print("FIzzBUzz")
    elif i % 3 == 0:
        print("FiZZ")
    elif i % 5 == 0:
        print("BuZZ")
    else:
        print(f"Value: {i}")

# printing strings in a list
fruits:[str] = ["apple",'orange','banana','guava','dragonFruit','pear','coconut','peach','grapes']
for fruh in fruits:
    print(f'eating {fruh}')
else:
    print(f"AAHHH, Greed has me choking now!! :><")

# random
for i in (1,2,3,4):
    print(i)

for i in [1,2,3,4]:
    print(i)

for i in "1234":
    print(i)

for i in range(1,5): # if not specified, it takes 0 as the starting index!
    print(i)

# Using Iterator
listOfValues_2 = range(1,101) # this is iterable as well!
iteratorForList_2 = iter(listOfValues_2)
while 1:
    try:
        print(next(iteratorForList_2))
    except StopIteration:
        print("OOps, guess we are done here!")
        break

listOfValues_2 = list(range(101))
iteratorForList_2 = iter(listOfValues_2)
while True:
    try:
        print(next(iteratorForList_2))
    except:
        print("Oh MOMMM!")
        break

listOfValues_2 = tuple(range(101))
iterand = iter(listOfValues_2)
while True:
    try:
        print(next(iterand))
    except:
        print("THE END")
        break
# if we don't use try-except with an iterator, we get the following error:
"""
    Traceback (most recent call last):
        File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/Chapter_3_CodeSnippets.py", line 81, in <module>
            print(next(iterand))
    StopIteration
"""
# the for-loop automates the above process

# using generators
# calculating Prime-Factors of a number
def primeFactorCalc(num:int):
    factor = 2
    while factor * factor <= num:
        if num%factor:
            factor+=1
        else:
            num//=factor
            yield factor
    if num > 1:
        yield num
valueForCalculation:int = 3000
print(f"Prime-Factorization of {valueForCalculation} is",end="-> ")
for i in primeFactorCalc(valueForCalculation):
    print(i,end=", ")
print("\n--------------------------------------------------------------")

# Recursion
# calculating prime-factors
def pF(num, fact=2):
    if fact*fact > num > 1:
        return [num]
    if num%fact == 0:
        return [fact] + pF(num//fact,fact)
    else:
        return pF(num,fact+1)
print(f"Prime Factorization of 3000: {pF(3000)}")
print(f"Prime Factorization of 2: {pF(2)}")
print(f"Prime Factorization of 3: {pF(3)}")
print(f"Prime Factorization of 4: {pF(4)}")
print(f"Prime Factorization of 6: {pF(6)}")
print(f"Prime Factorization of 12: {pF(12)}")
print(f"Prime Factorization of 15: {pF(15)}")
print(f"Prime Factorization of 100: {pF(100)}")

## Factorial using Linear Recursion
def calcFactorial(n:int):
    if n == 1:
        return 1
    return n * calcFactorial(n-1)
print(f"Factorial of 5: {calcFactorial(5)}")

## Binary Recursion to calculate Array sum
#looking into it
"""
def arraySum(arr:[int], begin:int, size:int ): # binary sum
    if n == 1:
        return arr[begin]
    return arraySum(arr,begin,int(math.ceil(size/2.0))) + arraySum(arr,int(begin+math.ceil(size/2.0)),int(math.floor(size/2.0)))

"""
numbers:[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum:int = 0
for i in numbers:
    sum+=i
print(f"Sum of array: for-loop ->{sum}, recursion -> ")#{arraySum(numbers,0,len(numbers))}")

# binary recur to calc fibonacci numbers
def BinaryFib(n:int):
    if 0 <= n < 2:
        return n
    return BinaryFib(n-1) + BinaryFib(n-2)
print(f"Fibonacci number 10: {BinaryFib(10)}")

# linear recur to calc fibonacci numbers
def LinearFib(n:int):
    if n<=1:
        return 1,0
    curr,prev = LinearFib(n-1)
    return curr+prev,curr
print(f"Fibonacci number 10: {LinearFib(10)[0]}")
