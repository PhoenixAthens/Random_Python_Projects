Tree:[str] = ["A",["B",["D",[],[]],[]],["C",["E",["G",[],[]],[]], ["F",[],[]]]]
def treeRoot(aTree):
    if aTree:
        return aTree[0]

def treeLeft(aTree):
    if aTree:
        return aTree[1]

def treeRight(aTree):
    if aTree:
        return aTree[2]

print(f"Root: {treeRoot(Tree)}")
print(f"Left-subtree: {treeLeft(Tree)}")
print(f"Right-subtree: {treeRight(Tree)}")
print("Inorder-Traversal of tree gives us: ")
def inorderTraversal(tree):
    if tree:
        inorderTraversal(tree[1])
        print(tree[0],end=", ")
        inorderTraversal(tree[2])

inorderTraversal(Tree)
print()
def inorderTraversal_FromBook(tree):
    if tree:
        inorderTraversal_FromBook(treeLeft(tree))
        print(treeRoot(tree),end=", ")
        inorderTraversal_FromBook(treeRight(tree))

inorderTraversal_FromBook(Tree)
print()
def preOrderTraversal(tree):
    if tree:
        print(treeRoot(tree),end=", ")
        preOrderTraversal(treeLeft(tree))
        preOrderTraversal(treeRight(tree))
print("The Pre-order traversal of tree gives us: ",end="[")
preOrderTraversal(Tree)
print("]")

def postOrderTraversal(tree):
    if tree:
        postOrderTraversal(treeLeft(tree))
        postOrderTraversal(treeRight(tree))
        print(treeRoot(tree),end=", ")

print("The postorder traversal of tree gives us: ",end="[")
postOrderTraversal(Tree)
print("]")

# Breadth-First Traversal
def BFS(treeGraph):
    if treeGraph:
        qList = [treeGraph]
        while qList:
            currentNode = qList.pop(0) #  otherwise this would pop the last element appended to the queue
            if currentNode:
                print(treeRoot(currentNode),end=" ")
                qList.append(treeLeft(currentNode))
                qList.append(treeRight(currentNode))
print("BFS of binary tree gives us",end=" -> ")
BFS(Tree)
print()

""" BUG Fixing
listing = [1,2,3]
print(listing.pop(0))
listing.append(4)
print(listing.pop(0))
print(listing)
"""

# Linear Search
def linearSearch(numList, keyValue):
    index = 0
    listLen = len(numList)
    while index < listLen:
        if numList[index] == keyValue:
            return index
        index+=1
    return -1

# Linear Search (ordered List)
def orderedLinearSearch(numList:[int], keyValue:int)->int:
    success : bool = False
    stop: bool = False
    lenOfList: int = len(numList)
    index: int = 0

    while index<lenOfList and not stop and not success:
        if numList[index]==keyValue:
            success = True
        elif numList[index] > keyValue:
            stop = True
        else:
            index+=1
    return success

# Binary Search
def BinarySearch(numList, keyValue):
    left = 0;
    right = len(numList) - 1
    while left <= right:
        mid = (left+right)//2
        if keyValue == numList[mid]:
            return mid
        elif keyValue > numList[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1

# insertion Sort
def insertionSort(arr:[int]):
    lengthOfList:int = len(arr)
    for i in range(1,lengthOfList):
        currElement = arr[i]
        j:int = i
        while j>0:
            if currElement >= arr[j-1]:
                break
            arr[j]=arr[j-1]
            j-=1
        arr[j]=currElement

# Bubble Sort
def bubbleSort(arr : [int]):
    length : int = len(arr)-1
    for i in range(length,0,-1):
        swap : bool = False
        for j in range(0, i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
        else:
            swap = False

# Selection Sort
def selectionSort(arr : [int]):
    length : int = len(arr)-1
    for i in range(length,0,-1):
        maxIndex = 0
        for j in range(1,i+1):
            if arr[j]>arr[maxIndex]:
                maxIndex = j
        arr[maxIndex], arr[i] = arr[i], arr[maxIndex]

def quickSort(aList:[int]): # this is just a wrapper
    length = len(aList)-1
    qSort(aList,0,length) # this is the start of our function
def qSort(arr:[int], left:int, right:int):
    if left >= right:
        return
    partIndex = partition(arr,left,right) # this calculates our partition, our pivot (array's first element),
    # and swaps elements smaller than pivot to its left, greater than pivot to the right
    qSort(arr,left,partIndex-1) # this is the recursive call that takes care of sorting array to the left of pivot
    qSort(arr,partIndex+1,right) # this recursive call takes care of sorting array to the right of the pivot
def partition(arr:[int], left:int, right:int):
    pivot=arr[left] #the first element of array or its sub-arrays is choosen as the pivot
    # left pointer = i
    i = left + 1 # because 'left' is pivot we start our from an index after it
    # right pointer = j
    j = right
    while True: # this loop works until the left pointer is at index less than the right pointer
        while i<=j and arr[i] <= pivot: # this loop finds elements to the left of pivot that are greater than pivot
            i+=1 # "i" stores the index of faulty element on the left side of the pivot
        while i<=j and arr[j] >= pivot: # this loop finds elements to the right of the pivot that are less than pivot
            j-=1 # "j" stores the index of faulty element on the right side of the pivot
        # until we haven't encountered a problem where right-points becomes less than left-pointer
        # this if-conditional swaps faulty elements from left to right and from right to left
        if i <= j:
            arr[i],arr[j]=arr[j],arr[i]  # swap step
        else:
            break
    # once right pointer becomes less than left pointer we move our pivot between the left subarray and right subarray
    # by the time we reach this step below our left pointer has reached the index where arr[i] > pivot
    # and our right pointer has reached the index where arr[j] < pivot, thus we swap arr[j] with pivot
    arr[left],arr[j]=arr[j],arr[left]
    return j


sampleList:[int] = [3, 5, 7, 9, 12, 15, 18, 21, 23, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55]
print(BinarySearch(sampleList,49)) # 17
print(BinarySearch(sampleList,15)) # 5
print(BinarySearch(sampleList,39)) # -1

sampleList_2: [int] = [-17, -1, 12, 13, 27, 45, 57, 82]
print(BinarySearch(sampleList_2,13))

sampleList_3: [int] = [45, 12, 67, 89, 34, 23, 90, 11, 56, 78, 3, 6, 9, 15, 18, 21, 24, 27, 30, 33]
insertionSort(sampleList_3)
print(sampleList_3)
# [3, 6, 9, 11, 12, 15, 18, 21, 23, 24, 27, 30, 33, 34, 45, 56, 67, 78, 89, 90]

sampleList_4 : [int] = [12,3,22,44,15,13,7,45,77,33]
insertionSort(sampleList_4)
print(sampleList_4)
# [3, 7, 12, 13, 15, 22, 33, 44, 45, 77]

sampleList_5 = [-17, -1, 12, 13, 27, 45, 57, 82]
sampleList_6 = [45, 12, 67, 89, 34, 23, 90, 11, 56, 78, 3, 6, 9, 15, 18, 21, 24, 27, 30, 33]
sampleList_7 = [12,3,22,44,15,13,7,45,77,33]
bubbleSort(sampleList_5)
bubbleSort(sampleList_6)
bubbleSort(sampleList_7)
print(f" SampleList_5: {sampleList_5}")
print(f" SampleList_6: {sampleList_6}")
print(f" SampleList_7: {sampleList_7}")
"""
SampleList_5: [-17, -1, 12, 13, 27, 45, 57, 82]
SampleList_6: [3, 6, 9, 11, 12, 15, 18, 21, 23, 24, 27, 30, 33, 34, 45, 56, 67, 78, 89, 90]
SampleList_7: [3, 7, 12, 13, 15, 22, 33, 44, 45, 77]
"""

sampleList_8 = [-17, -1, 12, 13, 27, 45, 57, 82]
sampleList_9 = [45, 12, 67, 89, 34, 23, 90, 11, 56, 78, 3, 6, 9, 15, 18, 21, 24, 27, 30, 33]
sampleList_10 = [12,3,22,44,15,13,7,45,77,33]
insertionSort(sampleList_8)
insertionSort(sampleList_9)
insertionSort(sampleList_10)
print(sampleList_8)
print(sampleList_9)
print(sampleList_10)

sampleList_11 = [12,3,22,44,15,13,7,45,77,33]
quickSort(sampleList_11)
print(sampleList_11)