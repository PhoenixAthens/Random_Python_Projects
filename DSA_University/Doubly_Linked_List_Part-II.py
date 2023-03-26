# Doubly Linked List
class DoubleHeadedNode:
    def __init__(self, value, prevNode, nextNode):
        self.val=value
        self.prev: DoubleHeadedNode=prevNode
        self.next: DoubleHeadedNode=nextNode

class DoublyLinkList:
    def __init__(self):
        self.length: int=0
        self.Head: DoubleHeadedNode=DoubleHeadedNode(None,None,None)
        self.Tail: DoubleHeadedNode=DoubleHeadedNode(None,None,None)

    def isEmpty(self)->bool:
        return True if self.length == 0 else False

    def getLength(self)->int:
        return self.length

    def addElement(self, value)->None:
        if self.length==0:
            self.Head = self.Tail = DoubleHeadedNode(value, None, None)
        else:
            node = DoubleHeadedNode(value, None, self.Head)
            self.Head.prev = node
            self.Head=node
        self.length+=1

    def addToFront(self, value):
        if self.isEmpty():
            self.addElement(value)
        else:
            node = DoubleHeadedNode(value, None, self.Head)
            self.Head.prev = node
            self.Head = node
            self.length += 1

    def addToLast(self, value):
        if self.isEmpty():
            self.addElement(value)
        else:
            node = DoubleHeadedNode(value,self.Tail,None)
            self.Tail.next=node
            self.Tail=node
            self.length+=1

    def createArray(self)->[int]:
        node = self.Head
        arrayFromList: [int] = []
        while node is not None:
            arrayFromList.append(node.val)
            node = node.next
        return arrayFromList

ListOfNodes = DoublyLinkList()
ListOfNodes.addToFront(999)
print(ListOfNodes.createArray())
ListOfNodes.addElement(23)
print(ListOfNodes.createArray())
ListOfNodes.addElement(46)
ListOfNodes.addElement(92)
ListOfNodes.addElement(184)
ListOfNodes.addElement(368)
print(ListOfNodes.createArray())
ListOfNodes.addToFront(736)
print(ListOfNodes.createArray())
ListOfNodes.addToLast(1472)
print(ListOfNodes.createArray())