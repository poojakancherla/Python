from BaseBinaryTree import Node

t = Node(object)

root = t.Tree()

def preOrder(root):
    if root:
        print(root.value)
        preOrder(root.left)
        preOrder(root.right)

print(preOrder(root))
