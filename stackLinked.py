class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def isEmpty(self):
        return self.top is None

    def pop(self):
        if self.isEmpty():
            print('STACK UNDERFLOW')
            return

        else:
            popped = self.top
            self.top = self.top.next
            popped.next = None
            return popped.data

    def peek(self):
        if self.isEmpty():
            print('STACK UNDERFLOW')
            return 

        return self.top.data

    def printStack(self):
        if self.isEmpty():
            print("STACK UNDERFLOW")
            return

        else:
            current = self.top
            print('-------------THE STACK----------------')
            while current:
                print(current.data,end="\n")
                current = current.next
            print('-------------------------------------')

s = Stack()

while True:
    print('1.Push\n2.Pop\n3.Peek\n4.PrintStack\n5.Exit\nChoose the operation:')
    choice = int(input())
    if choice == 1:
        value = input('enter the value: ')
        s.push(value)
        print('value pushed into the stack')
        print('------------------------------')
    elif choice == 2:
        print(f'the popped item is {s.pop()}')
        print('--------------------------------')
    elif choice ==3:
        print(f'the top of the stack is {s.peek()}')
        print('-------------------------------------')
    elif choice == 4:
        s.printStack()
    
    else:
        break

    
