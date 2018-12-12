# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# A utility function to do post order tree traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

# A utility function to do pre order tree traversal
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# A utility function to search a given key in BST
def search(root,key):
    # Base case: root is null or key is present at root
    if root.val == key or root is None:
        return root
    else:
        # Key is greater than root's key
        if root.val < key:
            return search(root.right, key)
        # Key is smaller than root's key
        return search(root.left, key)

# Driver program to test the above functions
head = Node(4)
insert(head, Node(2))
insert(head, Node(6))
insert(head, Node(1))
insert(head, Node(3))
insert(head, Node(5))
insert(head, Node(7))

preorder(head)

print("________________")

print(search(head, 3).val)
