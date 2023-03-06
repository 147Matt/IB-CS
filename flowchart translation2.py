collection=[3,1,4,2]
i=1

while i< len(collection):
    value=collection[i]
    j=i-1
    while j>=0 and collection[j]>value:
        collection[j+1]= collection[j]
        j=j-1
    collection[j+1]=value
    i=i+1
print(collection)