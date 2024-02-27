# function to do bubble sort
def bubble_sort(arr):

    # loop through the array
    for i in range(len(arr)):
        # loop through the array
        for j in range(0, len(arr)-i-1):
            # if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                # swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Iteration ",i+1,arr)
    return arr


# call the method with the array
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))