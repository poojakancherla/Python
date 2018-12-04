from BaseBinaryTree import Node

t = Node(object)
root = t.Tree()

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value)
        inOrder(root.right)
print(inOrder(root))
