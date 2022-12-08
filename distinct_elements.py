def countdistinct(arr):
    count=0
    for i in range(len(arr)):
        flag=False
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                flag=True
                break
        if flag==False:
            count+=1
    return count
#driver code
arr=[8,4,6,7,3,4,8,9,8]
print("count is :",countdistinct(arr))