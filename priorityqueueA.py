class PriorityQueue:
    def __init__(self):
        self.priorityqueue=[]

    def enqueue(self,value,priority):
        self.priorityqueue.append((value,priority))
        self.priorityqueue.sort(key=lambda x:x[1],reverse=True)

    def dequeue(self):
        return self.priorityqueue.pop(0)[0]

    def size(self):
        return len(self.priorityqueue)

    def display(self):
        for items,priority in self.priorityqueue:
            print(items,end=' ')

pq = PriorityQueue()
pq.enqueue('nagendra', 2)
pq.enqueue('marisetti', 4)
pq.enqueue('venkata',3)
pq.enqueue('babu',1)
pq.display()