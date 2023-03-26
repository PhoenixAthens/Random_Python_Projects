class DoubleLinkedList:
    # Not the proper implementation of a Doubly-LinkedList
    class DNode:
        def __init__(self, value=None, prev=None, next=None):
            self.val=value
            self.prevNode=prev
            self.nextNode=next

        def getValue(self):
            return self.val
        def getPreviousNode(self):
            return self.prevNode
        def getNextNode(self):
            return self.nextNode
        def setPreviousNode(self, node):
            self.prevNode=node
        def setNextNode(self, node):
            self.nextNode=node
    def __init__(self):
        self.length=0
        self.Head=DoubleLinkedList.DNode()
        self.Tail=DoubleLinkedList.DNode()
    def isEmpty(self):
        return True if self.length==0 else False
    def getLength(self):
        return self.length
    def addNode(self, element: DNode, prevElement: DNode, nextElement: DNode):
        if self.isEmpty():
            self.Head = self.Tail = DoubleLinkedList.DNode(element, None, None)
        else:
            tempNode = DoubleLinkedList.DNode(element, prevElement, nextElement)
            if self.length ==1:
                self.Head.nextNode=tempNode
                self.Tail=tempNode
                self.Tail.prevNode=self.Head
            else:
                prevElement.nextNode = tempNode
                if nextElement is not None:
                    nextElement.prevNode = tempNode


        self.length+=1
    def deleteNode(self,elem:DNode):
        lastNode: DoubleLinkedList.DNode = elem.prevNode
        nextNode: DoubleLinkedList.DNode = elem.nextNode
        lastNode.nextNode=nextNode
        nextNode.prevNode=lastNode
        self.length-=1
    def addNodeFront(self, elem):
        self.addNode\
            (elem,self.Head,self.Head.nextNode)

    def addNodeLast(self, elem):
        # this is adding element right before tailNode
        self.addNode\
            (elem,self.Tail.prevNode,self.Tail)

    def createList(self)->[int]:
        tempHead=self.Head
        arrayFromList: [int] = []
        while tempHead is not None:
            arrayFromList.append(tempHead.val)
            tempHead=tempHead.nextNode
        return arrayFromList

makeList = DoubleLinkedList()
makeList.addNodeFront(23)
makeList.addNodeFront(46)
makeList.addNodeFront(92)
makeList.addNodeFront(100)
makeList.addNodeFront(234)
makeList.addNodeLast(56)
makeList.addNodeLast(112)
makeList.addNodeFront(46)
print(makeList.createList())
print(makeList.Tail.val)
"""

makeList.addNodeFront(92)
makeList.addNodeFront(100)
makeList.addNodeFront(234)
makeList.addNodeLast(56)
makeList.addNodeLast(112)
print(makeList.createList())

"""
