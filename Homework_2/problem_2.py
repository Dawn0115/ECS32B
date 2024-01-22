'''
    File Name: problem_2 in Howmework 2
    Description: This program is used to search for an item in an array one by one
    Author: YANGCHENG
    Date: 1/29
'''
def sequential_search(input_list, target):
    # using a for loop to iterate the input list
    for i in range(len(input_list)):
        #check if the current number equal the target
        if input_list[i] == target:
            target_index = i
            # break the loop and return the current numbers' index.
            return target_index
    # there is no target in this loop, then return -1
    return -1

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(sequential_search(my_list, 3))  # Correct Output: 2
    print(sequential_search(my_list, 0))  # Correct Output: -1
    #TODO (optional): Your testing code here


'''
The best case is the target number is in the first place in the whole list. So we can find the target in the first time loop.
The computational complexity is O(1)


The worst case is the target number is in the last place in the whole list. So we have to iterate the entire loop to find this target.
The computational complexity is O(n), {n is the number of items in the list}


The average case is the average times this program need to find the target. So the computational complexity is also O(n), {n is the number of items in the list}

'''