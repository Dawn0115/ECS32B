def radix_sort(arr):
    # Get the maximum value in the array
    max_val = max(arr)

    # Get the number of digits in the maximum value
    max_digits = len(str(max_val))

    # Apply counting sort to each digit
    for digit in range(max_digits):
        # Initialize a counting array
        count = [0] * 10

        # Count the occurrences of each digit
        for num in arr:
            digit_val = (num // 10 ** digit) % 10
            count[digit_val] += 1

        # Calculate the cumulative sum of the counts
        for i in range(1, 10):
            count[i] += count[i-1]

        # Build a sorted array
        sorted_arr = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            digit_val = (arr[i] // 10 ** digit) % 10
            count[digit_val] -= 1
            sorted_arr[count[digit_val]] = arr[i]

        # Update the original array
        arr = sorted_arr

    return arr
arr = [3,6,1,4,9,8]
print(radix_sort(arr))
