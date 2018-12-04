class BinaryTree(object):

# First, we set the attributes
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

# When inserting a left child, we check if the root has any left childself.
# If it does not, then simply insert it. If it does, then we will move the existing child one level down
# and then insert the new child
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

# Symmetric to left child insertion
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

# Some methods to get thr root value, left and right child nodes. Also to set a new value to the root
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, newVal):
        self.value = newVal

    def getRootVal(self):
        return self.value


r = BinaryTree(1)
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft(4)
print(r.getLeftChild().getRootVal())
