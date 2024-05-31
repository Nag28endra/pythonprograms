class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListAtBeginning:
    def __init__(self):
        self.head = None
        self.Length = 0
    
    def addData(self,data):
        newNode = Node(data)
        self.data = data
        if self.head is None:
            self.head = newNode
            self.Length =1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.Length +=1

    def insert_at_beginning(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def getLength(self):
        return self.Length

    def printList(self):
        current = self.head 
        while current is not None:
            print(current.data,end="->")
            current=current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def insert_at_position(self,position,data):
        if position < 0 or position > self.Length:
            return "Invalid position"
        else:
            new_node = Node(data)
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                for i in range(position-1):
                    current = current.next
                new_node.next = current.next
                current.next = new_node

linkedList = LinkedListAtBeginning()
linkedList.addData(12)
linkedList.addData(28)
linkedList.addData(23)
linkedList.addData(32)
linkedList.insert_at_beginning(7)
linkedList.insert_at_end(42)

print(f'the length of the linked list is {linkedList.getLength()}')
linkedList.printList()

linkedList.insert_at_position(3, 44)

linkedList.printList()