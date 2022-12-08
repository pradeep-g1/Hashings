def intersection(arr1,arr2):
    result=[]
    for i in arr1:
        if i in arr2:
            result.append(i)
    return result
arr1=[5,8,5,7,8,10]
arr2=[1,5,5,8,1,8,7]
x=intersection(arr1,arr2)
y=set(x)
print("intersection of two arrays: ",list(y))