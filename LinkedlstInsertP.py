class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListAtPosition:
    def __init__(self):
        self.head = None
        self.Length = 0

    def addData(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.Length = 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.Length +=1
    def delete_first(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            self.Length -= 1

    def insert_at_beginning(self,data):
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
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for i in range(position-1):
                    current = current.next
                newNode.next = current.next
                current.next = newNode

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current =current.next
        print("None")

    def getLength(self):
        return self.Length
    
    def deleteLast(self):
        # Check if the linked list is empty
        if self.head is None:
            print("Linked List is empty")
            return
        # Check if the linked list has only one node
        elif self.head.next is None:
            self.head = None
            self.Length -= 1
        else:
            # Iterate through the linked list until the second last node is reached
            current = self.head
            while current.next.next is not None:
                current = current.next
            # Set the next of second last node to None to delete the last node
            current.next = None
            self.Length -= 1


linkedlst = LinkedListAtPosition()

linkedlst.addData(12)
linkedlst.addData(28)
linkedlst.addData(7)
linkedlst.addData(23)
print('actual linked List:')
linkedlst.printList()

linkedlst.insert_at_beginning(18)
print('linked list after insertion at beginning:')
linkedlst.printList()

linkedlst.insert_at_end(44)
print('linked list after insertion at the end')
linkedlst.printList()

linkedlst.insert_at_position(3, 27)
print('final linked list:')
linkedlst.printList()
print(f"length : {linkedlst.getLength()}")
print('linked list after deletion of first node:')
linkedlst.delete_first()
linkedlst.printList()
print('list after deleting last node:')
linkedlst.deleteLast()
linkedlst.printList()
