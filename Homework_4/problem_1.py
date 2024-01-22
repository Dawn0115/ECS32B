'''
    File Name: Successor and predecessor in tree    
    Description: return the asked value bybinary search
    Author: Yang Cheng
    Date:3/3
'''
'''
    HW4 P1
    Please don't change any function names
'''
# Node definition provided, please don't modify it.
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
# TODO: Please implement the following functions that return an integer

# Return the smallest value in the tree that is bigger than given value. Return -1 if not found.
def successor(root, value):
    
    if not root:
        return -1
        #creat a empty list to store all numbers that are bigger than given value.
    L = []
# determine if the node has value or it is a null node.
    while root:
        # compare two numbers 
        if root.val > value:
            # store the value if it is greater than given value
            L.append(root.val)
            root  = root.left
        # else move the right node of this root node.
        else:
            root = root.right
    #check whether the list is empty
    if len(L) != 0:
        #find the smallest number in this list by executing python built in function min()
        return min(L)
    else: 
        return -1
        
# Return the largest value in the tree that is smaller than given value. Return -1 if not found.
def predecessor(root, value):
    if not root:
        return -1
         #creat a empty list to store all numbers that are smaller than given value.
    G = []
   
    # determine if the node has value or it is a null node.
    while root:
         # compare two numbers 
        if root.val < value:
             # store the value if it is greater than given value
            G.append(root.val)
            root = root.right
        else:
            root = root.left
    if len(G) != 0:
         #find and return the biggest number in this list by executing python built in function min()
        return max(G)
    else: 
        return -1

if __name__ == "__main__":
    # TODO: (Optional) your test code here.
    my_root = TreeNode(3)
    my_root.left = TreeNode(1)
    my_root.right = TreeNode(5)
    my_root.right.left = TreeNode(4)
    print(successor(my_root, 2))  # expected 3
    print(predecessor(my_root, 2))  # expected 1
    print(successor(my_root, 3))  # expected 4


''''
Output is:
3
1
4

'''