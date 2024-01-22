'''
    File Name: transform a stack to queue based on Queue class
    Description: A class used to creat a queue, and modify it
    Author: YANG CHENG
    Date: 1/13
'''

class Queue:
    '''
    TODO: Remove the "pass" statements and implement each method
    Add any methods if necesssary
    DON'T use any builtin queue class to store your items
    '''
    def __init__(self): # Constructor function
        self.items = []
    def isEmpty(self): # Returns True if the queue is empty or False otherwise
        if self.items == []:
            return True
        else:
            return False
    def len(self): # Returns the number of items in the queue
         return len(self.items)
    def peek(self): # Returns the item at the front of the queue
        return self.items[0]
    def add(self, item): # Adds item to the rear of the queue
        self.items.append(item)
    def pop(self): # Removes and returns the item at the front of the queue
        a = self.items.pop(0)
        return a
    #remove the specific index number and return the result
    def remove(self, index): # Removes and returns the item at index of the queue
        result = self.items[index]
        self.items.pop(index)
        return(result)

# the fuction used to trasform stack to queue
def stackToQueue(stk):
    '''input stack will be in the form of a list. Implement your LinkedQueue. 
    We will pop() the elements and compare with the LIFO order of the stack
    '''
    queue = Queue()
    # determine if we have finished iterating
    while len(stk) != 0:
        b = stk.pop()
        queue.add(b)
    return queue
if __name__ == "__main__":
    stack = [1,2,3]
    res=stackToQueue(stack)
    print(res.pop()) #the autograder will use your Queue's pop() function, append to a list and compare with initial stack.
    '''
    Correct output of res would be a LinkedQueue in the order 3, 2, 1'''