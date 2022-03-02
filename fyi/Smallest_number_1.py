def small(x):
    b=x[0]
    for i in range(1,len(x)):
        if(x[i]<b):
            b=x[i]
            
    return b
list_1=[4,3,2,1]
print(small(list_1))
            
        
#min

list_1=[4,3,2,1]
print(min(list_1))

#sort

list_1=[4,3,2,1]
list_1.sort()
print(list_1[0])
