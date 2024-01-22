'''
    File Name: problem_4 in Homework 2
    Description: Sorting a listing in descending order by selection sort.
    Author: YANGCHENG
    Date: 1/29
'''
def selection_sort(input_list, reverse):
    # first for loop to iterare the whole list
    for i in range(len(input_list)):
        MAX = i 
        # create another list to compare remaining numbers with the number we iterate
        for k in range(i+1, len(input_list)):
            if reverse == True:
                # if we find a larger number, then swap the location of these two numbers
                if input_list[k] > input_list[MAX]:
                    MAX = k
            if reverse == False:
                if input_list[k] < input_list[MAX]:
                    MAX = k
        input_list[i], input_list[MAX] = input_list[MAX], input_list[i]
    return input_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(selection_sort(my_list, True))  # Correct Output: [5, 4, 3, 2, 1]
    #TODO (optional): Your testing code here

'''
Since we create a nested for loop go over the entire loop, and compare each numbers with the iterating number, first for loop will run n times, but the second for loop will only run n-1 times, so the toal run time is n times n.
Computational complexity    O(n*(n-1)) = O(n suqared minus n)
'''