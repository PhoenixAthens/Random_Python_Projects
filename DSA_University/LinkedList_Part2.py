
class LinkedList:
    class Node:
        def __init__(self, val):
            self.value = val
            self.NextNode = None
        def setCurrentValue(self, newValue):
            self.value=newValue
        def setNextNode(self,node):
            self.NextNode=node
        def getValue(self):
            return self.value
        def getNextNode(self):
            return self.NextNode

    # this list is pushing new elements to the beginning of the list
    # say you add an element, 1 to the list that has the following structure: [ 2, 3, 4]
    # adding an element makes it so [1, 2, 3, 4]

    def __init__(self):
        self.length=0
        self.Head: LinkedList.Node=None
    def isEmpty(self):
        return True if self.length==0 else False
    def getLength(self):
        return self.length
    def addNode(self,value):
        node = self.Node(value)
        node.setNextNode(self.Head)
        self.Head=node
        self.length+=1

    def deleteNode(self,elementValue):
        if self.length == 0:
            print("The list is empty")
            return False
        flag: bool = False
        tempNode: LinkedList.Node=self.Head
        lastNode: LinkedList.Node = None
        while tempNode is not None:
            if tempNode.value == elementValue:
                if lastNode is None:
                    self.Head = tempNode.NextNode
                else:
                    lastNode.setNextNode(tempNode.NextNode)
                flag = True
                self.length-=1
                break
            else:
                lastNode = tempNode
                tempNode = tempNode.NextNode

        if flag:
            print("Element was deleted!")
            return True
        else:
            print("Element not found!")
            return False
    """
    A simplified version of method deleteNode()
    
    def deleteNode(self,elementValue):
        if self.length == 0:
            return False
        tempNode: LinkedList.Node=self.Head
        lastNode: LinkedList.Node = None
        while tempNode is not None:
            if tempNode.value == elementValue:
                if lastNode is None:
                    self.Head = tempNode.NextNode
                else:
                    lastNode.setNextNode(tempNode.NextNode)
                return True
            else:
                lastNode = tempNode
                tempNode = tempNode.NextNode
        return False
        
    """
    def printList(self):
        ListArray: [int] = []
        tempHead=self.Head
        while tempHead is not None:
            ListArray.append(tempHead.value)
            tempHead=tempHead.NextNode
        return ListArray

    def SearchNode(self, elementValue):
        tempHead: LinkedList.Node = self.Head
        while tempHead is not None:
            if tempHead.value == elementValue:
                return True
            else:
                tempHead = tempHead.NextNode
        return False

list = LinkedList()
list.addNode(12)
list.addNode(13)
list.addNode(45)
list.addNode(67)
list.addNode(90)
list.addNode(77)
arrayFromList: [int] = list.printList()
print(f"List: {arrayFromList}")  # List: [77, 90, 67, 45, 13, 12]
print(f"Does list contain 12: {list.SearchNode(12)}")
print(f"Does list contain 11: {list.SearchNode(11)}")
print(type(list))
print(f"Is List Empty: {list.isEmpty()}")
print(f"Length of list: {list.getLength()}")
list.deleteNode(45)
print(f"Current state of list: {list.printList()}")
print(f"Length of list: {list.getLength()}")
list.deleteNode(35)
print(f"Current state of list: {list.printList()}")
print(f"Length of list: {list.getLength()}")