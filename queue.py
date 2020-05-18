
class Queue(object):
    def __init__(self,maxsize):
        self.q = [[] for i in range(maxsize)]
        self.maxsize = maxsize
        self.size = 0
        self.front = self.rear = 0
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def isFull(self):
        if self.size == self.maxsize:
            return True
        else:
            return False
    
    def Enqueue(self,x):
        if not self.isFull():
            self.q[self.rear] = x
            self.rear += 1
            self.size += 1
        else:
            print("[ERROR] Queue is full!")
    
    def Dequeue(self):
        if not self.isEmpty():
            print("Dequeued item is:",self.q[self.front])
            self.front += 1
            self.size -= 1
        else:
            print("[ERROR] Queue is already empty!")
    
    def show(self):
        for i in range(self.size):
            print(self.q[i+self.front],end=' ')
        print("\n")
    
q1 = Queue(10)
q1.Enqueue(20)
q1.Enqueue(30)
q1.Enqueue(9)
q1.Enqueue(51)
q1.Enqueue(52)
q1.Enqueue(56)
q1.show()
q1.Dequeue()
q1.Dequeue()
q1.show()


        
