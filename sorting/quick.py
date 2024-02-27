# function to perform quick sort
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot=[x for x in arr[1:] if x<=pivot]
        greater_than_pivot=[x for x in arr[1:] if x>pivot]
        return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)
arr = [4,8,1,9,2,7,3,10,2]
print(quick_sort(arr))
