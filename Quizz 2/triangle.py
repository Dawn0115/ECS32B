
def pascaltriangle():
    
    #the first row in this triangle is fixed
    #create a nested list
    triangle = [[1]]
#iterate each line of this triangle 
    for i in range(1, 6):
        # Create a new row with the first and last elements set to 1
        row = [1]
        #iterate each number in each line
        for j in range(1, i):
            # Calculate the current element as the sum of the two elements above it
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        # append 1 at last in each row
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    triangle.remove([1,1])
    # Print the triangle
    for row in triangle:
        # add a space between each integer
        print(' '.join(map(str, row)))
    

pascaltriangle()
'''
Output looks like:
1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''
