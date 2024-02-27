# function to do selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Iteration ", i+1, ":", arr)
    return arr

array = [64, 25, 12, 22, 11]
print(selection_sort(array))