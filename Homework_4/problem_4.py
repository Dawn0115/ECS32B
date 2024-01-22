'''
filename: preorder,postorder, and inorder traversal
author: YANG CHENG
Date: 3/4
'''

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
    def preorder(self): # Node-> Left->Right
        print(self.val, end=",")
        # check whether it is node which contain value
        if self.left:
            #recursive to left
            self.left.preorder()
            #then recursive to right
        if self.right:
             self.right.preorder()
    def postorder(self): # Left->Right->Node
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val, end=",")

    # Inorder Traversal
    def inorder(self):# Left->Node->Right
        if self.left:
            self.left.inorder()
        print(self.val, end=",")
        if self.right:
            self.right.inorder()

if __name__ == "__main__":
    R = TreeNode(25)
    R.left = TreeNode(15)
    R.right = TreeNode(50)
    R.left.left = TreeNode(10)
    R.left.right = TreeNode(22)
    R.right.left = TreeNode(35)
    R.right.right = TreeNode(70)
    R.left.left.left = TreeNode(4)
    R.left.left.right = TreeNode(12)
    R.left.right.left = TreeNode(18)
    R.left.right.right = TreeNode(24)
    R.right.left.left = TreeNode(31)
    R.right.left.right = TreeNode(44)
    R.right.right.left = TreeNode(66)
    R.right.right.right = TreeNode(90)
    R.preorder()
    print()
    R.postorder()
    print()
    R.inorder()

'''Output is
25,15,10,4,12,22,18,24,50,35,31,44,70,66,90,
4,12,10,18,24,22,15,31,44,35,66,90,70,50,25,
4,10,12,15,18,22,24,25,31,35,44,50,66,70,90,
'''