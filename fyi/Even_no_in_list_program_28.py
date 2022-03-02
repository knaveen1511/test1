def even(x):
    count=[]
    for i in x:
        if(i%2==0):
            count.append(i)
    return count
list_1=[2,7,5,64,14]
print(even(list_1))
