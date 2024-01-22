'''
    File Name: Heap sort
    Description: heap sort
    Author: YANGCHENG
    Date:3/3


HW4 P2
'''
# sort a heap by treating it as a list
def heap_sort(L):
    #creat a list to store sorted value
    result = []
    #iterate the whole list
    for i in range(len(L)):
        #find the maximum value 
        k = max(L)
        # insert the maximum value to new list in the beginning
        result.insert(0,k)
        #remove that value in original list
        L.remove(k)
    return result

q = [3,6,4,67,8,9,4,6,2]
print(heap_sort(q))

'''output is:
[2, 3, 4, 4, 6, 6, 8, 9, 67]

'''
