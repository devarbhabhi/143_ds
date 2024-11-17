class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
