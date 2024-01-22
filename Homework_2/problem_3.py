'''
    File Name: problem_3 in Homework 2
    Description: A programm that by reversing a list without reverse method
    Author: YANGCHENG
    Date: 1/29
'''
def reverse_elems(input_list):
    #creat an empty list to store the reversed items.
    reversed_list = []
    # use a for loop to iterate the entire list and at each time, insert the item in original list in the first place of the reversed list.
    for i in input_list:
        reversed_list.insert(0, i)
    return reversed_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(reverse_elems(my_list))  # Correct Output: [5, 4, 3, 2, 1]
    #TODO (optional): Your testing code here


'''
Since there is only one for loop to go through the input list,so the computational complexity is O(n), n is the number of itmes in input list.


'''