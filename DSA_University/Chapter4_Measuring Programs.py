# Difficulties in Python (Dynamic typing)
from random import randint
def typeCheck(num):
    if num%2:
        a = 123
    else:
        a = "123"
    print(type(a))
typeCheck(randint(1,1000))

# Cyclomatic Complexity ( CC(G) = e-v+2k ), where e = edges, v = vertices, and k = components
def findMax(num1:int, num2:int, num3:int)->int:
    if num1 > num2: # A
        maxNum = num1 # B
    else:
        maxNum = num2 # C
    if maxNum < num3: #D
        maxNum = num3 #E
    return maxNum #F
# Cyclomatic complexity of control structure in above function is:
"""
    A
   / \
  B   C
  \  /
   D
  /| 
 E |
 \ |
  F
Edges (e) = 7
Vertices (v) = 6
Components (k) = 1
Therefore, CC(G) = 7 - 6 + 2x1 = 3
"""

# if we add a redundant branch to the control structure, we ge the following
def findMax_2(num1:int, num2:int, num3:int)->int:
    if num1 > num2: # A
        maxNum = num1 # B
    else:
        maxNum = num2 # C
    if maxNum < num3: #D
        maxNum = num3 #E
    else:
        maxNum = num2 #F
    return maxNum #G
"""
    A
   / \
  B   C
  \  /
   D
  / \
 E   F
 \  /
   G
Edges (e) = 8
Vertices (v) = 7
Components (k) = 1
Therefore, CC(G) = 8-7+2X1 = 3
"""


