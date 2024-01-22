'''
    File Name: Stack
    Description: create a stack and einput_strecuting modification
    Author: YANG CHENG
    Date: 2/12
'''
# A class used to create a stack, then then define some functions to modify it.
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
        
# determine whether the input string ispalindrome.
def palindrome(input_str):
    stk = []
    #  input string with even length
    if len(input_str) % 2 == 0:
        for i in range(0,len(input_str)):
            if i<int(len(input_str)/2):
                stk.append(input_str[i])
            elif stk.pop()!=input_str[i]:
                return False
        if len(stk)>0:
            return False
        return True
    #input string with odd length
    else:
        for i in range(0,len(input_str)):
            if i==int(len(input_str)/2):
                continue
            elif i<int(len(input_str)/2):
                stk.append(input_str[i])
            elif stk.pop()!=input_str[i]:
                return False
        if len(stk)>0:
            return False
        return True

if __name__ == "__main__":
    my_str = "noon"
    print(palindrome(my_str))  # Correct Output: True
    #TODO (optional): Your testing code here

'''
 print(palindrome("noon"))
 Output is True
print(palindrome("Hello"))
Output is False

STK = Stack()
STK.push(Alpha)
print(STK)
Output is Alpha

print(len(STK))
Output is 5

ptint(isempty(STK))
Output is False

'''