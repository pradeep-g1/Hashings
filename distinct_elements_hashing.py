def countdistinct(arr):
    s=set()
    for i in range(len(arr)):
        s.add(arr[i])
    return len(s)
#driver code
arr=[2,4,3,2,5,7,8,3,8]
print("count is: ",countdistinct(arr))