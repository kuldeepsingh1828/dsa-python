# function to do binary search
def binarySearch(li,val):
    low = 0
    high = len(li)-1
    while low<=high:
        mid = (low+high)//2
        if li[mid]==val:
            return mid
        elif li[mid]<val:
            low = mid+1
        else:
            high = mid-1
    return -1

index = binarySearch([2, 3, 5, 7, 8, 9, 10],11)
print(index)