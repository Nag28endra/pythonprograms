class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def printTree(node,level=0):
    if node is not None:
        printTree(node.right,level=level+1)
        print(" "*4*level+"->",node.data)
        printTree(node.left,level=level+1)

root = Node("542")
root.right=Node("503")
root.left = Node('504')
root.right.right = Node('502')
root.right.left = Node('525')
root.left.right = Node('507')
root.left.left = Node('513 ')
printTree(root)
