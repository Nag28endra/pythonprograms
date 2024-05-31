class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)
    return root

def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root

def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level=level+1)
        print(" " * 4 * level + "->", root.key)
        print_tree(root.left, level=level+1)

root = None
root = insert_node(root, 50)
root = insert_node(root, 30)
root = insert_node(root, 20)
root = insert_node(root, 40)
root = insert_node(root, 70)
root = insert_node(root, 60)
root = insert_node(root, 80)

print("Initial tree:")
print_tree(root)

root = delete_node(root, 20)
print("Tree after deleting 20:")
print_tree(root)

root = delete_node(root, 30)
print("Tree after deleting 30:")
print_tree(root)

root = delete_node(root, 50)
print("Tree after deleting 50:")
print_tree(root)
