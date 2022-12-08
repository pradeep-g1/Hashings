def freq(arr):
    map=dict()
    for i in range(len(arr)):
        if arr[i] in map.keys():
            map[arr[i]]+=1
        else:
            map[arr[i]]=1
    for i in map:
        print(i,":",map[i])
arr=[9,2,2,3,4,4,5,9,9]
freq(arr)