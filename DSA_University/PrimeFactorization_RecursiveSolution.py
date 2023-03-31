import sys
sys.setrecursionlimit(6000)
# the line above will fix recursion depth issues when input is some value like 123456789
# It's better to use a loop
# Recursion works properly only if:
# 1. we first increase recursion depth
# 2. we create a method to check if the value is prime

def PrimeFactors(num, factor, listOf):
    if num < factor*factor:
        listOf.append(num)
        return listOf
    if num%factor > 0:
        PrimeFactors(num, factor+1, listOf)
    else:
        listOf.append(factor)
        PrimeFactors(num//factor,factor,listOf)
#lit= []
#PrimeFactors(123456789,2,lit)
#print(lit)

# 2^9 * 3 * 5^9
"""
Sure! Here are some large numbers that you can try to find the prime factorization of:
987654321 = 3^2 * 17^2 * 379721
123456789 = 3^2 * 3607 * 3803
999999937 = 
1000000007
4294967291
"""

# this solution with inputs like 123456789 results in exceeding depth of recursion, it's better to use while loop
def PrimeF(num, factor = 2):
    if num < factor*factor:
        return [num]
    if num%factor == 0:
        return [factor] + PrimeF(num//factor,factor)
    return PrimeF(num,factor+1)

print(PrimeF(999999937))