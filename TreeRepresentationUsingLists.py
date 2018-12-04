# First create the root node of the tree
def BinaryTree(root):
    return [root, [], []]

# If we want to insert a left child at a given root:
    # First pop the left sub tree of the root
    # If the subtree is not empty insert the new node as root at index 1 of the given root and
    # to this insert the left subtree to the left and an empty list to the right of the root (newNode)
    # If the subtree is empty, insert the new node and then two empty lists as left and right childs
    # index 1 here represents the left sub tree

def insertLeft(root, newNode):
    leftSubTree = root.pop(1)
    if len(leftSubTree) > 1:
        root.insert(1, [newNode, leftSubTree, []])
    else:
        root.insert(1, [newNode, [], []])
    return root

# Same as left child, except that the nodes are to inserted at index 2. Also, the right subtree
def insertRight(root, newNode):
    rightSubTree = root.pop(2)
    if len(rightSubTree) > 1:
        root.insert(2, [newNode, [], rightSubTree])
    else:
        root.insert(2, [newNode, [], []])
        return root

# Some common methods
def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
      return root[2]

#Creating a BST and inserting child nodes
root = BinaryTree(5)

insertLeft(root, 4)

insertRight(root, 6)

setRootVal(root, 1)

insertLeft(root, 2)

print(getRootVal(root))

print(insertLeft(root, 3))

print(getLeftChild([2, [4, [], []], []]))
