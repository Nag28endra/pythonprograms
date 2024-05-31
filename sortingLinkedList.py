class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SortLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
    
    def addElements(self,data):
            newNode = Node(data)
            if self.head is None:
                self.head = newNode
                # self.Length = 1
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = newNode
    
    def sortList(self):
        # check if list is empty or only contains one element
        if self.head is None or self.head.next is None:
            return

        # perform bubble sort
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
    
    def printList(self):
        if self.head is None:
            print('the list is empty:')
            return 
        else:
            current = self.head
           
            while current is not None:
                print(current.data,end="->")
                current = current.next
            print("None")

sList = SortLinkedList()
sList.addElements(28)
sList.addElements(11)
sList.addElements(23)
sList.addElements(2)
sList.addElements(1)
sList.addElements(10)

print('original list is :')
sList.printList()
sList.sortList()
print('sorted list is:')
sList.printList()

        