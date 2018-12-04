class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# When inserting a left child, we check if the root has any left childself.
# If it does not, then simply insert it. If it does, then we will move the existing child one level down
# and then insert the new child
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = Node(newNode)
        else:
            temp = self.leftChild
            temp.leftChild = Node(newNode)

# Symmetric to left child insertion
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = Node(newNode)
        else:
            temp = self.rightChild
            temp.rightChild = Node(newNode)

# Some methods to get the root value, left and right child nodes. Also to set a new value to the root
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, newVal):
        self.value = newVal

    def getRootVal(self):
        return self.value


# Binary Tree to be used in Tree Traversals
    def Tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)

        return root

    def fillBinaryTree(self):
        rootNode = Node(input())
