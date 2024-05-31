class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedListDelete:
    def __init__(self):
        self.head = None
        self.Length = 0

    def addData(self,data):
            newNode = Node(data) 
            if self.head is None:
                self.head = newNode
                # self.Length = 1
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = newNode
            self.Length +=1
        
    def insert_at_beg(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode
        self.Length +=1

    def insert_at_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.Length +=1

    def insert_at_position(self,position,data):
        if position<0 or position>self.Length:
            return "Invalid Position"

        else:
            newNode = Node(data)
            if position==0:
                self.head = newNode

            else:
                current = self.head

                for i in range(position-1):
                    current = current.next
                newNode.next = current.next
                current.next = newNode
            self.Length +=1

    def deleteFirst(self):
        if self.head is None:
            print('the list is empty')
            return

        else:
            self.head = self.head.next
            self.Length -=1
    
    def deleteEnd(self):
        if self.head is None:
            print('the list is empty')
            return 

        elif self.head.next is None:
            self.head = None
        
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
        self.Length -=1

    def deleteAtPosition(self,position):
        if self.head is None:
            print('the list is empty')
            return

        elif position == 0:
            self.head = self.head.next

        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            current.next = current.next.next
            self.Length -=1

    def printList(self):
        if self.head is None:
            print('the list is empty')
            return 
        
        else:
            current = self.head
            while current is not None:
                print(current.data,end='->')
                current = current.next
               
        print("None")

    def getLength(self):
        return self.Length
        
linkedLst = LinkedListDelete()

linkedLst.addData(502)
linkedLst.addData(503)
linkedLst.addData(504)
linkedLst.addData(507)
print('the original linked List is :')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')
print()

linkedLst.insert_at_beg(542)
print('list after the insertion at first:')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')
print()

linkedLst.insert_at_end(525)
print('list after the insertion at the end:')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')
print()

linkedLst.insert_at_position(2, 513)
print('list after the insertion at a position')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')
print()

linkedLst.deleteFirst()
print('list after the deletion of first node:')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')
print()

linkedLst.deleteEnd()
print('list after the deletion of last node:')
linkedLst.printList()
print(f'length:{linkedLst.getLength()}')

linkedLst.deleteAtPosition(1)
print('list after the deletion of node at a position:')
linkedLst.printList()
print(f'length: {linkedLst.getLength()}')
