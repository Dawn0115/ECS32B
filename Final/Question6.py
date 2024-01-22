class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Traverse a tree DFS style.
def traverse(root):
    
    # List that represents visited order.
    ret = []
    
    def dfs(node):
        # TODO: Implement DFS algorithm here
        #creat a stack and input the root in it initially
        stack=[root]
        #check if there are items in stack
        while stack:
            #set current node as the value poped from stack
            node=stack.pop()
            if node:
                ret.append(node.val)
                #append node.right first can pop the node.right last
                stack.append(node.right)
                #append node.left last can pop the node.left first
                stack.append(node.left)
    dfs(root)
    return ret


def main():
    nodes = [None] * 9
    for i in range(9):
        nodes[i] = TreeNode(i+1)
    # Tree construction
    # 5
    nodes[4].left = nodes[3]
    nodes[4].right = nodes[5]
    # 4
    nodes[3].left = nodes[1]
    # 2
    nodes[1].left = nodes[0]
    nodes[1].right = nodes[2]
    # 6
    nodes[5].right = nodes[7]
    # 8
    nodes[7].left = nodes[6]
    nodes[7].right = nodes[8]

    root = nodes[4]
    print(traverse(root))


if __name__ == "__main__":
    main()

'''Output is:
[5, 4, 2, 1, 3, 6, 8, 7, 9]'''