# Given a binary tree, check whether it’s a binary search tree or not.

from BaseBST import genTree

def BSTCheck(root):
    if not root: return True

    def checkValid(root):
        # checks if there is a left child and if it's less that the parent
        if root.left and root.left.val > root.val: return False
        # checks if there is a right child and if it's greater that the parent
        if root.right and root.right.val < root.val: return False
        # if no children, return true
        return True

    def checkNode(root):
        if not root: return True # if node is not present

        if checkValid(root): # if a node is valid, then check if it's left and right nodes are valid
            checkNode(root.left)
            checkNode(root.right)
        else:
            return False
        return True

    return checkNode(root)

root = genTree("[5, 3, 6, 1, 4]")
print(BSTCheck(root))
