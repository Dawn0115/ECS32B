'''
    File Name: praser class
    Description: use tree to do calculation
    Author: YANGCHENG
    Date:3/3
'''
'''
    HW4 P2
    Please don't change any function names
    Add any methods if necesssary
    TODO: Remove the pass statements and implement the methods. 
'''
# assign value for leaf node
class LeafNode:
    def __init__(self, data):
        self.data = data
    def postfix(self):
        return str(self)
    def __str__(self):
        return str(self.data)
    def prefix(self):
        return str(self.data)
    def infix(self):
        return str(self.data)
    def value(self):
        return self.data
class InteriorNode:
    def __init__(self, op, left_op, right_op):
        self.op = op
        self.left_op = left_op
        self.right_op = right_op
    #execute in post order LRN(left->right->node)
    def postfix(self):
        return self.left_op.postfix() + " " + self.right_op.postfix() + " " + self.op
        #execute in preorder NLR(Node->left->right)
    def prefix(self):
        return self.op + " " + self.left_op.prefix() + " " + self.right_op.prefix()
        #execute in inorder LNR (left->node->right)
    def infix(self):
        return "(" + self.left_op.infix() + " " + self.op + " " + self.right_op.infix() + ")"
    def value(self):
        L = self.left_op.value()
        R = self.right_op.value()
        #do the calculation by determine the opration signs in node, and return the mathched value
        if self.op == '+':
            return L + R
        elif self.op == '-':
            return L - R
        elif self.op == '*':
            return L * R
        elif self.op == '/':
            return L / R
if __name__ == "__main__":
    # TODO: (Optional) your test code here.
    a = LeafNode(4)
    b = InteriorNode('+', LeafNode(2), LeafNode(3))
    c = InteriorNode('*', a, b)
    c = InteriorNode('-', c, b)
    print("Expect ((4 * (2 + 3)) - (2 + 3)) :", c.infix())
    print("Expect - * 4 + 2 3 + 2 3 :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + - :", c.postfix())
    print("Expect 15 :", c.value())

'''
Output is:
Expect ((4 * (2 + 3)) - (2 + 3)) : ((4 * (2 + 3)) - (2 + 3))
Expect - * 4 + 2 3 + 2 3 : - * 4 + 2 3 + 2 3
Expect 4 2 3 + * 2 3 + - : 4 2 3 + * 2 3 + -
Expect 15 : 15

'''