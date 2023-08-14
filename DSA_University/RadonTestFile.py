def linearSearch(numToFind:int, elementList: [int])->int:
    length = len(elementList)
    for i in range(0,length):
        if elementList[i] == numToFind:
            return i
    return -1
def typeCheck(num:int):
    if num%2: # odd
        x = 123
    else: # even
        x = "123"
    print(type(x))
def testMax(num1:int, num2:int, num3:int):
    if num1 > num2:
        maxNum = num1
    else:
        maxNum = num2
    if num3 > maxNum:
        maxNum = num3
    return maxNum

typeCheck(2)