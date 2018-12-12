class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.val)
        inorder(root.right)

# Function to delete a node with the given key
def deleteNode(root, key):

    if root is None: return root # If no root, return None

    if key < root.val: # If key is less than root, traverse to the left of root in order to find the key
        root.left = deleteNode(root.left, key)

    elif key > root.val: # If key is greater than root, traverse to the right of root in order to find the key
        root.right = deleteNode(root.right, key)

    else: # If key is equal to the root, means we have to delete the root
    # There are 3 poosibilities here

        if root.right is None: return root.left # If no right child, then the left node replaces the root

        elif root.left is None: return root.right # If no left child, then the right node replaces the root

        # if the root has both left and right child
        curr = root.right # the smallest node in the right subtree replaces the node
        while(curr.left):
            curr = curr.left # finding the smallest node
        root.val = curr.val # replace root value
        root.left = deleteNode(root.left, root.val) # Delete the smallest node that replaced the root

    return root

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)
