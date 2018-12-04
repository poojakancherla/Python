from BaseBinaryTree import Node

t = Node(object)
root = t.Tree()

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value)

print(postOrder(root))
