class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):

    if root == None:
        root == node
    else:
        if node.val <= root.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        if node.val > root.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

head = Node(4)
insert(head, Node(2))
insert(head, Node(6))
insert(head, Node(1))
insert(head, Node(3))
insert(head, Node(5))
insert(head, Node(7))


def LevelOrder(root):
    if root is None:
        print('Nothing')
    # Add the node to a queue
    q = [root]
    while q: # while the queue has elements
        root = q.pop() # Remove the first element and set it as the root
        print(root.val, end=' ') # print it

        # Process next level
        if root.left: # If the root has left child
            q.insert(0, root.left) # Add it to the queue
        if root.right: # If the root has right child
            q.insert(0, root.right) # Add it to the queue

LevelOrder(head)
