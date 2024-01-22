'''
    File Name: Problem_6 in Homework2
    Description: The comparison between original quick sort and modified version
    Author: YANGCHENG
    Date: 1/30
'''
# use random mudule to create random list that used to test difference between two sort
import random
import time
def creat_random_list(size):
    L = []
    for i in range(size):
        Num = random.randint(1,size)
        if not Num in L:
            L.append(Num)
    return L

# codes to execute insertion sort if there are only 50 less items in list
def insertion_sort(lyst):
    i = 0
    # check if we go through the whole list
    while i < len(lyst):

        insert_item = lyst[i]
        j = i -1
        while j >= 0:
            if insert_item < lyst[j]:
                # swap two numbers in correct order.
                lyst[j+1] = lyst[j]
                j-=1
            else:
                break
        lyst[j+1] = insert_item
        i = i + 1
    return lyst

# def changed quicksort
def modified_quicksort(input_list):
    sorted_list = []
    # if there are less than 50 items we tend to use insertion sort to sort list
    if len(input_list) < 50:
        sorted_list = insertion_sort(input_list)
        return sorted_list
    else:
        quicksort(input_list, 0, len(input_list) - 1)
        return input_list

def quicksort(lyst, first, last):
    if first < last:
        PivotLO = exchangeLo(lyst, first, last)
        quicksort(lyst, first, PivotLO-1)
        quicksort(lyst, PivotLO+1, last)
        return lyst
#exchange the location of pivot and first and last item
def exchangeLo(lyst, first, last):
    #find Pivot
    middleindex = (first + last) // 2
    Pivot_number = lyst[middleindex]
    #exchange the the location of pivot with last item
    lyst[middleindex] = lyst[last]
    lyst[last] = Pivot_number
    #make a boundary at left, move the numbers that are less than pivot to left
    boundary = first
    for i in range(first, last):
        if lyst [i] < Pivot_number:
            Adjust(lyst, i, boundary)
            boundary +=1
    Adjust(lyst, last, boundary)
    return boundary
def Adjust(lyst, a, b):
    prompt = lyst[a]
    lyst[a] = lyst[b]
    lyst[b] = prompt

   


        
def original_quicksort(input_list):
    quicksort(input_list, 0, len(input_list) - 1)
    return input_list
def quicksort(lyst, first, last):
    if first < last:
        PivotLO = exchangeLo(lyst, first, last)
        quicksort(lyst, first, PivotLO-1)
        quicksort(lyst, PivotLO+1, last)
def exchangeLo(lyst, first, last):
    #find Pivot
    middleindex = (first + last) // 2
    Pivot_number = lyst[middleindex]
    #exchange the the location of pivot with last item
    lyst[middleindex] = lyst[last]
    lyst[last] = Pivot_number
    #make a boundary at left, move the numbers that are less than pivot to left
    boundary = first
    for i in range(first, last):
        if lyst [i] < Pivot_number:
            Adjust(lyst, i, boundary)
            boundary +=1
    Adjust(lyst, last, boundary)
    return boundary
def Adjust(lyst, a, b):
    prompt = lyst[a]
    lyst[a] = lyst[b]
    lyst[b] = prompt

if __name__ == "__main__":
    my_list = [3, 4, 1, 5, 2]
    print(original_quicksort(my_list))  # Correct Output: [1, 2, 3, 4, 5]
    print(modified_quicksort(my_list))  # Correct Output: [1, 2, 3, 4, 5]



# start from this line, i measure the complexity of two sorts by importing time module.
'''def test():
    start = time.time()
    original_quicksort(creat_random_list(50))
    print(time.time()-start)
    start = time.time()
    modified_quicksort(creat_random_list(50))
    print(time.time()-start)

    start = time.time()
    original_quicksort(creat_random_list(500))
    print(time.time()-start)
    start = time.time()
    modified_quicksort(creat_random_list(500))
    print(time.time()-start)

    start = time.time()
    original_quicksort(creat_random_list(5000))
    print(time.time()-start)
    start = time.time()
    modified_quicksort(creat_random_list(5000))
    print(time.time()-start)
test()
'''
'''
The result of this test()funciton is:
4.1961669921875e-05
3.62396240234375e-05
0.0008039474487304688
0.0007317066192626953
0.043073177337646484
0.041889190673828125


if the threshold is 30, result is 
3.075599670410156e-05
2.193450927734375e-05,
In coclusion, if the threshold of using insertion sort is 30, it will be faster for this program to run.
'''