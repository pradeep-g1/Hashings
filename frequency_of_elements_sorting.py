def freq(arr):
    arr.sort()
    i=0
    while i<len(arr):
        count=1
        while i < len(arr)-1 and arr[i]==arr[i+1]:
            i+=1
            count+=1
        print("{0} : {1}".format(arr[i],count))
        i+=1
arr=[8,9,8,9,3,2,1,0,3,3]
freq(arr)
