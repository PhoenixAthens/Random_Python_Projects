#imperative programming
# partitioning an array (Algo - 1)

arrayOfInts = [11,59,26,17,2,1,25,9,3,15]
pivot = arrayOfInts[0]
i = 1
j = len(arrayOfInts)-1
while True:
    while i<=j and arrayOfInts[i]<=pivot:
        i+=1
    while i<=j and arrayOfInts[j]>pivot:
        j-=1
    if i<=j:
        arrayOfInts[i],arrayOfInts[j]=arrayOfInts[j],arrayOfInts[i]
    else:
        arrayOfInts[0], arrayOfInts[j] = arrayOfInts[j], arrayOfInts[0] # this was not in book's code
        break
print(arrayOfInts)
# book's code output:
## [11, 3, 9, 1, 2, 17, 25, 26, 59, 15]
# my code's output:
## [2, 3, 9, 1, 11, 17, 25, 26, 59, 15]

# above algorithm as a function:
arrayOfInts_2 = [11,59,26,17,2,1,25,9,3,15]
def partition(list:[int], pivot:int)->[int]:
    i = 1
    j = len(list)-1
    while True:
        while i<=j and list[i]<=pivot:
            i+=1
        while i<=j and list[j]>pivot:
            j-=1
        if i<=j:
            list[i],list[j] = list[j],list[i]
        else:
            #list[j],list[0]=list[0],list[j]
            break
    print(list)

partition(arrayOfInts_2,arrayOfInts_2[0])
# book's code output:
## [11, 3, 9, 1, 2, 17, 25, 26, 59, 15]
# my code's output:
## [2, 3, 9, 1, 11, 17, 25, 26, 59, 15]

# Object-oriented implementation of Above algorithm
class Scores:
    def __init__(self, List:[]):
        self.arr = List

    def length(self):
        return len(self.arr)

    def isEmpty(self):
        return self.arr == []

    def part(self):
        if self.isEmpty():
            return []
        else:
            pivot = self.arr[0]
            i = 1
            j = self.length()-1
            while True:
                while i<=j and self.arr[i]<=pivot:
                    i+=1
                while i<=j and self.arr[j]>pivot:
                    j-=1
                if i<=j:
                    self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
                else:
                    break
            self.arr[0],self.arr[j]=self.arr[j],self.arr[0]
            return self.arr

makeNew = Scores([11,59,26,17,2,1,25,9,3,15])
print(makeNew.part())
#Ouput - [2, 3, 9, 1, 11, 17, 25, 26, 59, 15]

# Functional programming in Python
a = lambda x: x+12
print(a(23)) # 35

print((lambda x: x*234)(34)) # 7956

sampleList:[int] = []
for i in range(1,100):
    sampleList.append(i)
print(sampleList)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
# 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
# 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
# 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
sampleList_2 = list(map(lambda x:x>23,sampleList))
#we used list() function because
# map() returns a map object which is an iterable
print(sampleList_2)
#[False, False, False, False, False, False, False, False, False,
# False, False, False, False, False, False, False, False, False,
# False, False, False, False, False, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True,
# True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
sampleList_3 = list(map(lambda x:x*23,sampleList))
print(sampleList_3)
#[23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345,
# 368, 391, 414, 437, 460, 483, 506, 529, 552, 575, 598, 621, 644, 667,
# 690, 713, 736, 759, 782, 805, 828, 851, 874, 897, 920, 943, 966, 989,
# 1012, 1035, 1058, 1081, 1104, 1127, 1150, 1173, 1196, 1219, 1242, 1265,
# 1288, 1311, 1334, 1357, 1380, 1403, 1426, 1449, 1472, 1495, 1518, 1541,
# 1564, 1587, 1610, 1633, 1656, 1679, 1702, 1725, 1748, 1771, 1794, 1817,
# 1840, 1863, 1886, 1909, 1932, 1955, 1978, 2001, 2024, 2047, 2070, 2093,
# 2116, 2139, 2162, 2185, 2208, 2231, 2254, 2277]
from functools import reduce
UsingReduce = reduce(lambda a,b:a*b,sampleList_3)
print(UsingReduce) # 604031267679412416290568705372884598921722249689930366133750985047991348062428854452605369784236074234749399906353868048489012620171954720603857260394042654486138302553086913901980065394602058331549197936727283515550906866774028751490698497382112887195018215120625991680000000000000000000000

UsingReduce_2 = reduce(lambda a,b:a+b, sampleList_3)
print(UsingReduce_2) # 113850

UsingFilter = list(filter(lambda a: a%3==0 or a%5==0,sampleList_3)) # because filter returns a filter object
print(UsingFilter)

UsingFilter_2 = list(filter(lambda a: a%3==0 and a%5 ==0,sampleList_3))
print(UsingFilter_2)

# partitioning problem using lambdas
sampleList_4 = [11,59,26,17,2,1,25,9,3,15]
partitionedList = (lambda listy: list(filter(lambda x: x<=listy[0],listy)) + list(filter(lambda x: x>listy[0],listy)))(sampleList_4)
print(partitionedList) #output - [11, 2, 1, 9, 3, 59, 26, 17, 25, 15]

partitionedList_improved = (lambda listy: list(filter(lambda x: x<listy[0],listy)) +[listy[0]] + list(filter(lambda x: x>listy[0],listy)))(sampleList_4)
print(partitionedList_improved) #output - [2, 1, 9, 3, 11, 59, 26, 17, 25, 15]

# Logic programming to solve the partitioning problem
"""
from kanren import run, eq, membero, var, conde
from kanren.arith import lt,gt
x = var()
L = [11,59,26,17,2,1,25,9,3,15]
pivot = L[0]
a = run(0, x, (membero, x, L), (lt, x, pivot)) # lt = less than
b = run(0, x, (membero, x, L), (eq, x, pivot)) # eq = equal
c = run(0, x, (membero, x, L), (gt, x, pivot)) # gt = greater than
d = run(0, x, (membero, x, a+b+c))
print(d)
"""
# kanren is throwing error
"""
Traceback (most recent call last):
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/DSA_University/Programming_paradigms.py", line 141, in <module>
    from kanren import run, eq, membero, var, conde
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/venv/lib/python3.11/site-packages/kanren/__init__.py", line 7, in <module>
    from unification import (unify, reify, unifiable, var, isvar, vars, variables,
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/venv/lib/python3.11/site-packages/unification/__init__.py", line 1, in <module>
    from .core import unify, reify
  File "/Users/anmolkhanna/Downloads/To push On GIT/Python Projects/venv/lib/python3.11/site-packages/unification/core.py", line 2, in <module>
    from collections import Iterator
ImportError: cannot import name 'Iterator' from 'collections' (/opt/homebrew/Cellar/python@3.11/3.11.4_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/collections/__init__.py)
"""

# Data Stream Programming
# genFib is a generator and gives us a data stream
def genFib(howMany):
    one = 0
    other = 1
    counter = 0
    while counter<howMany :
        yield one
        another = one + other
        one = other
        other = another
        counter+=1
gen = genFib(100)
def printFib(generator, limit):
    current = next(generator)
    while current<limit:
        print(current,end=", ")
        current=next(generator)

printFib(gen,1_000_000_000)
print()
# Event driven programming
from tkinter import *
def clickButton():
    print("Button clicked!")
w = Tk()
l = Label(w,text="Event-Driven Programming")
b = Button(w,text="Click me!",command=clickButton)
l.pack()
b.pack()
w.mainloop()

print()

# global variables
global academia
academia = 23
print(academia)

academia = 33
print(academia)

print("=====")

yAndy = 1
def A():
    global yAndy
    yAndy = 23
    print(yAndy) # 23
A()
print(yAndy) # 23
print("=========")
# global3.py
panama = 1
print(panama)
def fun1():
    panama = 2
    print(panama)
    def fun2():
        panama = 3
        print(panama)
    fun2()
    print(panama)
fun1()
print(panama)