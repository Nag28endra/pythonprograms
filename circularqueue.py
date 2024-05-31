class CircularQueue:
    def __init__(self,k):
        self.k = k
        self.head = -1
        self.tail=-1
        self.queue =[None]*k

    def enqueue(self,data):
        if self.isFull():
            print("the queue is Full")
            return
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail+1)%self.k
        self.queue[self.tail] = data

    def dequeue(self):
        if self.head == -1:
            print("Queue is empty")
            return
        elif self.head == self.tail:
            data = self.queue[self.head]
            self.head = -1
            self.tail=-1

        else:
            data = self.queue[self.head]
            self.head = (self.head+1)%self.k
        return data

    def display(self):
        if self.head ==-1:
            print('Queue is empty')

        else:
            for x in range(self.head,self.tail+1):
                print(self.queue[x],end=' ')
    
    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return (self.tail+1)%self.k == self.head


# create a circular queue with size 5
cq = CircularQueue(5)

# enqueue elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

# queue is now full
# trying to enqueue more elements will result in an error
cq.enqueue(60)  # raises QueueFullError

# display the queue
cq.display()
