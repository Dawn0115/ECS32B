'''
    File Name: Queue
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
        self.items.pop(0)
        return self.items[0]
    #remove the specific index number and return the result
    def remove(self, index): # Removes and returns the item at index of the queue
        result = self.items[index]
        self.items.pop(index)
        return(result)

if __name__ == "__main__":
    queue = Queue()
    
    
    #TODO (optional): Your testing code here

    '''
    Q = Stack()
    Q.add('Morning')
    print(Q)
    Output is Morning

    print(Q.len)
    Output is q

    print(Q.isEmpty)
    Output is False

    Q.add('ghi')
    Q.add('yui')
    print(Q.remove(2))
    Output is yui
    
    
    
    
    '''