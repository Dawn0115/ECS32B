'''
    File Name: check if the different kinds of brackets matched based on stack class
    Description: A class used to creat a queue, and modify it
    Author: YANG CHENG
    Date: 1/13
'''
class Stack:
    '''
    TODO: Remove the "pass" statements and implement each method
    Add any methods if necesssary
    DON'T use any builtin stack class to store your items
    '''
    def __init__(self): # Constructor function
        # start with an empty stack
        self.items = []
    def isEmpty(self): # Returns True if the stack is empty or False otherwise
        if self.items == []:
            return True
        else:
            return False
    def len(self): # Returns the number of items in the stack
        return len(self.items)
    def peek(self): # Returns the item at the top of the stack
        return self.items[len(self.items)-1]
    def push(self, item): # Adds item to the top of the stack
        self.items.append(item)
    def pop(self): # Removes and returns the item at the top of the stack
        a = self.items.pop()
        return a 
    
def bracketsBalance(input_str,opening_list,closing_list):
    isBalanced = True
    stk=Stack()
    for i in input_str:
        # pushall opening bracket in input string
        if i in opening_list:
            stk.push(i)
        # when meet a close stirng.
        elif i in closing_list:
            # check if it matches the open brackets appeared in front
            Loc = closing_list.index(i)
            if (stk.isEmpty()) or (opening_list[Loc] != stk.pop()):
                return False
            else:
                return True
              
              
    if (not stk.isEmpty()):
        isBalanced = False
    return isBalanced


   
if __name__ == "__main__":
    my_str = "([{}])"
    opening_list=['(', '[', '{']
    closing_list=[')', ']', '}']
    print(bracketsBalance(my_str,opening_list,closing_list))  # Correct Output: 
False
    #TODO (optional): Your testing code here