
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.Length = 0

    def addData(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.Length = 1
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                
            current.next = new_node
            self.Length +=1

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data,end="->")
            current = current.next
        print("None")
    
    def getLength(self):
        return self.Length

linkedList = LinkedList()
linkedList.addData(12)
linkedList.addData(28)
linkedList.addData(20)
linkedList.addData(2)
linkedList.addData(22)

linkedList.printList()
print(f'the number of elements in the list are {linkedList.getLength()}')
