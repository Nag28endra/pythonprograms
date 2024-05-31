class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()

# Append some elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Print the linked list
linked_list.print_list()