class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class LinkedList:
    """
    TODO: Remove the "pass" statements and implement each method
    Add any methods if necessary
    DON'T use a builtin list to keep all your nodes.
    """
    def __init__(self):
        self.head = None  # The head of your list, don't change its name. It should be "None" when the list is empty.


    def insert(self, index, num): # insert num into the given index
        node = Node(num)
        if index == 0: # if the index is zero, it means we should add value in the begaining
            #replace the head valuw with added number
            node.next = self.head
            self.head = node
            return
            # normal sitatiaion
        CUR = self.head
        # use a for loop to iterate to the index we want
        for i in range(index-1):
            if CUR.next is None:
                raise IndexError
            CUR = CUR.next
# replace the node with inserted number
        node.next = CUR.next
        CUR.next = node  

    def delete(self, index):  # remove the node at the given index and return the deleted value as an integer
        # when we need to delete the head nodes of this list
        if index == 0:
            #set deleted value as the number in first node
            Deleted = self.head.val
            self.head = self.head.next
            return Deleted

        current_node = self.head
        #use a for loop to access the specifc index value
        for i in range(index-1):
            if current_node.next is None:
                raise ValueError
            current_node = current_node.next
            #raise an error when the current node is empty
        if current_node.next is None:
            raise ValueError
        Node_deleted = current_node.next
        Deleted = Node_deleted.val
        current_node.next = Node_deleted.next
        return Deleted
 
    def circularize(self):   # Make your list circular. This method can only be the last call of the autograder.
        # check if the list is empty
        if self.head is None:
            return
        # the list is not empty, set the current node head value
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        # point the last node to the head node
        current_node.next = self.head  
    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.val == value:
                return True
            current_node = current_node.next
        return False
    #get the total number of the list
    def len(self): 
        #create an empty variable to count nodes
        cont = 0 
        current_node = self.head 
        #use a while loop to iterate each node, and add 1 to cont each time
        while current_node: 
            cont += 1 
            current_node = current_node.next 
            return cont 
    def push(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node
    def isempty(self):
        return self.head is None


    
 
