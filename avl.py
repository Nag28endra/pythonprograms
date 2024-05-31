class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insertNode(self,root,key):
        if root is None:
            return Node(key)
        elif key<root.data:
            root.left = self.insertNode(root.left,key)
        else:
            root.right = self.insertNode(root.right,key)
        
        root.height = 1+max(self.getHeight(root.right),self.getHeight(root.left))
        balanceFactor = self.getBalance(root)

        if balanceFactor>1 and key<root.left.data:
            return self.rightRotation(root)
        if balanceFactor<-1 and key>root.right.data:
            return self.leftRotation(root)
        if balanceFactor>1 and key>root.left.data:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        if balanceFactor<-1 and key<root.right.data:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root) 
        return root
    
    def getHeight(self,root):
        if root is None:
            return 0
        return root.height

    def getBalance(self,root):
        if root is None:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)

    def leftRotation(self,z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        y.height= 1+max(self.getHeight(y.left),self.getHeight(y.right))
        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))

        return y

    def rightRotation(self,z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        y.height= 1+max(self.getHeight(y.left),self.getHeight(y.right))
        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))


        return y

    def display(self,root,level=0):
        if root is not None:
            self.display(root.right,level=level+1)
            print(" "*4*level+'->',root.data)
            self.display(root.left,level=level+1)

if __name__=='__main__':
    tree = AVLTree()
    root = None
    
    root = tree.insertNode(root, 10)
    root = tree.insertNode(root, 20)
    root = tree.insertNode(root, 30)
    root = tree.insertNode(root, 40)
    root = tree.insertNode(root, 50)
    root = tree.insertNode(root, 25)

    tree.display(root)
    
        

