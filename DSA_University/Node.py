class SinglyLinkedList:
    def __init__(self, elem: int):
        self.value: int = elem
        self.nextNode: SinglyLinkedList = None

    def getElement(self):
        return self.value

    def getNextNode(self):
        return self.nextNode

    def setValue(self, newValue: int):
        self.value = newValue

    def setNextNode(self, node):
        self.nextNode = node

    def createArray(self):
        array = []
        node = self
        while node is not None:
            array.append(node.value)
            node = node.nextNode

        return array


nodeList = SinglyLinkedList(23)
node2 = SinglyLinkedList(46)
nodeList.nextNode = node2
node3 = SinglyLinkedList(92)
node2.nextNode = node3
node4 = SinglyLinkedList(184)
node3.nextNode = node4
node5 = SinglyLinkedList(368)
node4.nextNode = node5
print(nodeList.createArray())
