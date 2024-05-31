class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListAtTheEnd:
    def __init__(self):
        self.head = None
        self.Length = 0

    def addData(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.Length =  1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.Length +=1

    def insert_at_beginning(self,data):
        newNode = Node(data)
        if self.head is Node:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self,data):
        newNode = Node(data)
        if self.head is Node:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.Length +=1

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current = current.next


        print('None')
    
    def getLength(self):
        return self.Length

linkedlst = LinkedListAtTheEnd()
linkedlst.addData(12)
linkedlst.addData(28)
linkedlst.addData(2)
linkedlst.addData(11)
linkedlst.addData(1)

linkedlst.insert_at_beginning(7)
linkedlst.insert_at_end(32)

linkedlst.printList()
print(f'length : {linkedlst.getLength()}')

