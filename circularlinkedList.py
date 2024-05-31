class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addElements(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head

        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode

    def insertFirst(self,data):
        newNode = Node(data)      
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head

        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

    def insertEnd(self,data):
        self.addElements(data)

    def insertAtPosition(self,position,data):
        if position<0:
            print('INVALID POSITION')
            return
        
        newNode = Node(data)
        if position ==1:
            self.insertFirst(data)

        current = self.head
        while current.next!=self.head and position-1>1:  
            current = current.next
            position -=1

        nextNode = current.next
        newNode.next = nextNode
        current.next = newNode

    def deleteFirst(self):
        if self.head is None:
            print('list is empty')
            return

        if self.head == self.tail:
            self.head,self.tail = None

        self.head = self.head.next
        self.tail.next = self.head

    def deleteLast(self):
        if self.head is None:
            print('list is empty')

        if self.head == self.tail:
            self.head,self.tail = None

        current = self.head
        while current.next !=self.tail:
            current = current.next
        current.next = self.head
        self.tail = current


    def deleteAtPosition(self,position):
        if self.head is None:
            print('list is empty')

        if position<0:
            print('invalid Position')

        if position==1:
            self.head = self.head.next
            self.tail.next = self.head

        current = self.head
        while position-1>1:
            current = current.next
            position -=1

        nextNode = current.next.next
        current.next = None
        current.next = nextNode
        

    def printList(self):
        if self.head is None:
            print('the list is empty:')
            return 
        else:
            current = self.head
            while current.next!=self.head:
                print(current.data,end = " ")
                current = current.next
            print(current.data)
            print()

clist = circularLinkedList()

while True:
    print('choose:\n1.add elements\n2.insert at First\n3.insert at last\n4.insert a position\n5.delete first Node\n6.delete last node\n7.delete at position\n8.Print\n9.exit')
    choice = int(input('enter the choice: '))
    
    if choice == 1:
        data = int(input("enter the value: "))
        clist.addElements(data)
        print('element inserted')
        print()

    elif choice ==2:
        data = int(input('enter the value:'))
        clist.insertFirst(data)
        print('element inserted')
        print()

    elif choice == 3:
        data = int(input('enter the value:'))
        clist.insertEnd(data)
        print('element is inserted')
        print()

    elif choice == 4:
        data = int(input('enter the value:'))
        position= int(input('enter the position:'))
        clist.insertAtPosition(position, data)
        print('element is inserted')
        print()

    elif choice ==5:
        clist.deleteFirst()
        print('element deleted')
        print()

    elif choice == 6:
        clist.deleteLast()
        print('element deleted')
        print()

    elif choice == 7:
        position = int(input('give the position:'))
        clist.deleteAtPosition(position)
        print() 

    elif choice == 8:
        print('the list is:')
        clist.printList()
        print()

    
    else:
        break

