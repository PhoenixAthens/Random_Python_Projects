class MaxHeap:
    def __init__(self):
        self.TreeArray=[]

    def isEmpty(self):
        return self.TreeArray == []

    def size(self):
        return len(self.TreeArray)

    def _parent(self,i):
        # this method gives the index of element that would
        # in a Binary-Tree structure sit at parent index for element at
        # index i
        return (i - 1) // 2

    def insert(self, element):
        # this method inserts an element and compares it with its parent
        # to check if element at parent is less than child, if not we move one
        # otherwise we exchange the elements and move up the chain to check the
        # parent's parent and so on.
        self.TreeArray.append(element)
        index = self.size() - 1
        while index>0:
            parent=self._parent(index)
            if self.TreeArray[parent]<self.TreeArray[index]:
                self.TreeArray[parent],self.TreeArray[index]\
                    =self.TreeArray[index],self.TreeArray[parent]
            else:
                break
            index=parent

    def _maxChild(self, index):
        if index*2+2 >= self.size():
            return index*2 + 1
        elif self.TreeArray[index*2+1]>self.TreeArray[index*2+2]:
            return index*2 + 1
        else:
            return index*2 + 2

    def extractMax(self):
        maxElement = self.TreeArray.pop(0)
        if self.size()!=0:
            lastElement = self.TreeArray.pop()
            self.TreeArray.insert(0, lastElement)
            i = 0
            # in the expression for while below, we do i*2 because the child index is
            # always i*2+1 , i*2+2 so if i*2 > size(), then for that index children node does not index
            while 2*i < self.size()-1:
                childMax=self._maxChild(i)
                if self.TreeArray[childMax] > self.TreeArray[i]:
                    self.TreeArray[childMax],self.TreeArray[i]=\
                        self.TreeArray[i],self.TreeArray[childMax]
                else:
                    break
                i=childMax
        return maxElement

    def reportMax(self):
        return self.TreeArray[0]

    def printHeap(self):
        print(self.TreeArray)

makeList=MaxHeap()
toSort=[57, 99, 63, 2, 31, 48, 80, 70, 14, 95,
        35, 23, 64, 50, 44, 58, 8, 11, 90, 61, 68,
        97, 25, 52, 46, 71, 55, 29, 76, 13, 93, 60,
        79, 38, 86, 22, 69, 16, 5, 83, 43, 74, 28,
        66 ,91 ,18 ,33 ,56 ,98 ,62 ,3 ,32 ,49 ,81 ,
        72 ,15 ,96 ,36 ,24 ,65 ,51 ,45 ,59 ,9 ,12 ,92
        ,67 ,100 ,26 ,53 ,47 ,73 ,54 ,30 ,77 ,19 ,94
        ,41 ,78 ,39 ,87 ,21 ,17 ,6 ,84 ,42 ,75]
i=0
while i<len(toSort):
    makeList.insert(toSort[i])
    i+=1

"""
makeList.insert(12)
makeList.insert(11)
makeList.insert(13)
makeList.insert(5)
makeList.insert(6)
makeList.insert(7)
"""
makeList.printHeap()
sortedList=[]
while makeList.size()>0:
    sortedList.append(makeList.extractMax())
print(sortedList)

