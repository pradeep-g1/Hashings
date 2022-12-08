def display_hash(hashtable):
    for i in range(len(hashtable)):
        print(i,end=" ")
        for j in hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
hashtable=[[] for i in range(7)] #just created the hashtable
def hashing(keyvalue):
    return keyvalue%len(hashtable)
def insert(hashtable,value):
    i=value%len(hashtable)
    hashtable[i].append(value)
def searchitem(hashtable,val):
    index=val%len(hashtable)
    for j in hashtable[index]:
        if j == val:
            print("{0} present in hashtable".format(val))
            return
    print("{0} not preent in hashtable".format(val))
def deleteitem(hashtable,val):
    index=val%len(hashtable)
    for j in hashtable[index]:
        if j==val:
            hashtable[index].remove(j)
            print("{0} removed from hashtable".format(val))
#Driver code
insert(hashtable, 3)
insert(hashtable, 8)
insert(hashtable, 5)
insert(hashtable, 1)
insert(hashtable, 10)
insert(hashtable, 6)
searchitem(hashtable,10)
deleteitem(hashtable,10)
searchitem(hashtable,10)
display_hash(hashtable)