def freq(arr):
    for i in range(len(arr)):
        flag=False
        count=0
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                flag=True
                break
            # The continue keyword is used to end the current iteration 
        # in a for loop (or a while loop), and continues to the next iteration.
        if flag==True:
            continue
        for j in range(0,i+1):
            if arr[i]==arr[j]:
                count+=1
        print("{0}:{1}".format(arr[i],count))
arr=[8,6,8,7,8,9,0,3,4,4]
freq(arr)