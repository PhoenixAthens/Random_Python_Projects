class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue == []
    def size(self):
        return len(self.queue)
    def enQueue(self, val):
        self.queue.insert(0,val)
    def deQueue(self):
        return self.queue.pop()
    def printQ(self):
        print(self.queue)
q= Queue()
q.enQueue(23)
q.enQueue(46)
q.enQueue(34)
q.enQueue(90)
q.enQueue(6)
q.printQ()
print(q.deQueue())
print(q.deQueue())
q.printQ()