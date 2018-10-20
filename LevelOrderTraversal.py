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

class queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()



def LevelOrder(root):
    #  Create a queue
    q = queue()
    if root is None:
        print('Nothing')
    # Add the nde to the queue
    q.enqueue(root)
    while(q.is_empty() == False): # while the queue has elements
        root = q.dequeue() # Remove the first element and set it as the root
        print(root.val, end=' ') # print it

        # Process next level
        if root.left: # If the root has left child
            q.enqueue(root.left) # Add it to the queue
        if root.right: # If the root has right child
            q.enqueue(root.right) # Add it to the queue

LevelOrder(head)
