import sys
sys.setrecursionlimit(10000)
def linFib(n):
    if n<=1:
        return 1,0
    else:
        current, prev = linFib(n-1)
        return current+prev, current

print(linFib(5000))