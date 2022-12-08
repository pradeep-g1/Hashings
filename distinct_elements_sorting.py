def distinctcount(arr):
    arr.sort()
    count=0
    i=0
    while i < len(arr):
        while i<len(arr)-1 and arr[i]==arr[i+1]:
            i+=1
        count+=1
        i+=1
    return count
#driver code
arr=[8,4,5,7,2,4,8,4,5]
print("count is: ",distinctcount(arr))