class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


head = Node(4)
insert(head, Node(2))
insert(head, Node(6))
insert(head, Node(1))
insert(head, Node(3))
insert(head, Node(5))
insert(head, Node(7))

preorder(head)
