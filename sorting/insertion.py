# function to perform insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr = [3,6,1,8,2,4,9,5,10]
print(insertion_sort(arr))