class Node:
    def __init__(self,data):
        self.data =data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self,data):
        newNode = Node(data)
        if self.front is None:
            self.front = self.rare =newNode

        else:
            self.rare.next = newNode
            self.rare = newNode

    def dequeue(self):
        if self.isEmpty():
            print('QUEUE IS EMPTY')
            return
        else:
            current = self.front
            self.front = current.next
            current.next = None

    def isEmpty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")

queue = Queue()
while True:
    choice = int(input("1.enqueue\n2.dequeue\n3.display\n4.Exit\nchoose the operation:"))
    if choice == 1:
        data = int(input('\nenter the value:'))
        queue.enqueue(data)
    elif choice ==2:
        queue.dequeue()

    elif choice ==3:
        print('\nthe queue is :')
        queue.display()

    else: 
        break
