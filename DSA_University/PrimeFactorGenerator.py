def primeFactorGenerator(num:int)->int:
    fact = 2
    while fact * fact <= num:
        if num%fact:
            fact+=1
        else:
            num//=fact
            yield fact

    if num > 1:
        yield num

listOfFactors = primeFactorGenerator(6)
iterator = iter(listOfFactors)
while True:
    try:
        print(next(iterator),end=" ")
    except StopIteration:
        break

print("\n")
listOfFactors = primeFactorGenerator(3_000)
iterator = iter(listOfFactors)
while True:
    try:
        print(next(iterator),end=" ")
    except StopIteration:
        break

print("\n")
# easy approach to iterating a generator
for i in primeFactorGenerator(999999937):
    print(i,end=" ")