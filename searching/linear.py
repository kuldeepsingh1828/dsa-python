# function to do linear search
def linearSearch(li,val):
    for i in range(len(li)):
        if li[i]==val:
            return i
    return -1

index = linearSearch([1,5,3,7,2,10,8,9],4)
print(index)
