class Stack:
    def __init__(self):
        self.elements=[]

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def topOfStack(self):
        return self.elements[len(self.elements)-1]

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        return self.elements.pop()

    def removeAllElements(self):
        self.elements=[]

    def printStack(self):
        print(self.elements)

stack = Stack()
print(stack.isEmpty())
stack.push(23)
stack.push(46)
stack.push(92)
stack.push(184)
stack.push(368)
stack.printStack()
print(stack.pop())
print(stack.topOfStack())
print(stack.size())
print(stack.isEmpty())
stack.removeAllElements()
print(stack.isEmpty())
stack.printStack()
