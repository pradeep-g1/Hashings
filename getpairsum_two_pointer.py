def getpair(arr,sum):
    set1=set()
    for i in range(len(arr)):
        if sum-arr[i] in set1:
            print(arr[i],sum-arr[i])
        set1.add(arr[i])
#driver code
arr=[10,2,15,2,9,3,4,12]
getpair(arr,13)