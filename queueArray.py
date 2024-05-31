class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def display(self):
        for x in self.queue:
            print(x,end=' ')
        print()

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
