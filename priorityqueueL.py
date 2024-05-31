class Node:
    def __init__(self,data,priority):
        self.data =data
        self.priority= priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self,data,priority):
        newNode = Node(data,priority)
        if self.isEmpty():
            newNode.next = self.front
            self.front = newNode
        else:
            current = self.front
            while current.next and priority>=current.next.priority:
                current = current.next
            newNode.next = current.next
            current.next = newNode
        
    def isEmpty(self):
        return not bool(self.front)

    def dequeue(self):
        if self.isEmpty():
            return None
            

        else:
            item = self.front.data
            self.front = self.front.next
            return item

    def display(self):
        current = self.front
        while current is not None:
            print(current.data,end=" ")
            current = current.next

pq = PriorityQueue()
pq.enqueue(28, 2)
pq.enqueue(12, 1)
pq.enqueue(2000, 3)
pq.display()