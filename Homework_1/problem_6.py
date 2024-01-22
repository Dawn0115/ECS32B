# name: YANGCHENG
# finish date: 1/17
 
# this function is used to merging two sorted lists to a big one list and sort the big lis bt using recursion.
 
def merge(first_list, second_list):
    # create an empty list to store two merging list
    final_list = []
    # use this while loop to determine is the tow list empty ?
    while first_list and second_list:
        # determine whose first number is small, and move it to the final list
        if first_list[0] < second_list[0]:
            final_list.append(first_list[0])
            # remove the first number.
            first_list.pop(0)
        else:
            final_list.append(second_list[0])
            second_list.pop(0)
    # add remaining numbers in two lists to the final list
    final_list += first_list
    final_list += second_list
    return final_list
'''
merge([1,2,4,5,7,8,9],[3,6,10,12])
Output looks like: [1,2,3,4,5,6,7,8,9,10,12]
'''

