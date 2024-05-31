class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addElements(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode 
    # print('element is added')

    def insertFirst(self,data):
        newNode = Node(data)
        if self.head is None:
            print('the List is empty')
            return
        
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            print('the list is empty')
            return

        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def insertAtPosition(self,position,data):
        if position<1:
            print('INVALID POSITION')
            return
        newNode = Node(data)

        if position == 1:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        current = self.head
        while current is not None and position-1>1:
            current = current.next
            position -=1
        
        prevNode = current
        nextNode = current.next
       
        nextNode.prev = newNode
        newNode.next = nextNode
        prevNode.next = newNode
        newNode.prev = prevNode

    def deleteFirst(self):
        if self.head is None:
            print('the List is Empty')
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None

        self.head = self.head.next
        self.head.prev = None

    def deleteLast (self):
        if self.head is None:
            print('the list is empty')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        self.tail = self.tail.prev
        self.tail.next = None

    def deleteAtPosition(self,position):
        if position < 0:
            print('INVALID POSITION')
            return

        if position == 1:
            self.head = self.head.next
            self.head.prev = None

        current = self.head
        while current is not None and position-1>1:
            current = current.next
            position -=1

        nextNode = current.next.next
        if nextNode is not None: #if the node is the last one in the list
            nextNode.prev = current
        else:
            self.tail = current
        current.next = nextNode

    def traverseForward(self):
        if self.head is None:
            print('LIST EMPTY')
            return
        
        current = self.head
        while current is not None:
            print(current.data,end=' ')
            current = current.next
        print()

    
    def traverseBackward(self):
        if self.head is None:
            print('LIST EMPTY')
            return
        
        current = self.tail
        while current is not None:
            print(current.data,end=' ')
            current = current.prev
        print()




dblist = doubleLinkedList()

while True:
    print('choose:\n1.add elements\n2.insert at First\n3.insert at last\n4.insert a position\n5.delete first Node\n6.delete last node\n7.delete at position\n8.traverse forward\n9.traverse backward\n10.Exit')
    choice = int(input('enter the choice: '))
    
    if choice == 1:
        data = int(input("enter the value: "))
        dblist.addElements(data)
        print('element inserted')
        print()

    elif choice ==2:
        data = int(input('enter the value:'))
        dblist.insertFirst(data)
        print('element inserted')
        print()

    elif choice == 3:
        data = int(input('enter the value:'))
        dblist.insertEnd(data)
        print('element is inserted')
        print()

    elif choice == 4:
        data = int(input('enter the value:'))
        position= int(input('enter the position:'))
        dblist.insertAtPosition(position, data)
        print('element is inserted')
        print()

    elif choice ==5:
        dblist.deleteFirst()
        print('element deleted')
        print()

    elif choice == 6:
        dblist.deleteLast()
        print('element deleted')
        print()

    elif choice == 7:
        position = int(input('give the position:'))
        dblist.deleteAtPosition(position)
        print()

    elif choice == 8:
        print('the list is:')
        dblist.traverseForward()
        print()

    elif choice == 9:
        print(' the list in reverse is:')
        dblist.traverseBackward()
        print()

    else:
        break





