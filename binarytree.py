class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insertNode(root,data):
    if root is None:
        return Node(data)
    elif data<root.data:
        root.left = insertNode(root.left, data)
    elif data>root.data:
        root.right = insertNode(root.right,data)
    return root

def deleteNode(root,data):
    if root is None:
        return root
    elif data<root.data:
        root.left = deleteNode(root.left,data)
    elif data > root.data:
        root.right = deleteNode(root.right,data)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        temp = find_min_node(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

def find_min_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def display(root,level=0):
    if root is not None:
        display(root.right,level=level+1)
        print(" "*4*level+"->",root.data)
        display(root.left,level=level+1)
        
    

def preorderTraversal(root):
    if root is not None:
        print(root.data,end="->")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.data,end="->")
        inorderTraversal(root.right)

def postorderTraversal(root):
    if root is not None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data,end="->")

def height(root):
    if root is None:
        return -1

    else:
        l_height = height(root.left)
        r_height = height(root.right)
        return 1 + max(l_height,r_height)

def countNodes(root):
    if root is None:
        return 0
    else:
        return 1+countNodes(root.left)+countNodes(root.right)


root = None
while True:
    print('---------------------------------------')
    choice = int(input("1.Insert\n2.Delete\n3.Display\n4.preorder traversal\n5.inorder traversal\n6.postorder traversal\n7.exit\n8.Heigth\n9.count nodes\nChoose the operation:"))
    print("---------------------------------------")
    if choice==1:
        value= input('\nenter the value:')
        root = insertNode(root, value)
    elif choice ==2:
         value =input('\nenter the value:')
         root = deleteNode(root,value)
    elif choice ==3:
        display(root)
    elif choice ==4:
        print('Preorder traversal:')
        preorderTraversal(root) 
        print('\n')
    elif choice == 5:
        print("Inorder Traversal")
        inorderTraversal(root)
        print('\n')
    elif choice ==6:
        print('Postorder Traversal')
        postorderTraversal(root)
        print('\n')
    elif choice == 8:
        print(f'height of the tree is: {height(root)}')
    elif choice ==9:
        print(f'no of nodes are:{countNodes(root)}')
    else:

        break

    