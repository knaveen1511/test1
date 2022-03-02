#for
def negative(x):
    for i in x:
        if(i<0):
            print("Negative",i)
    return 
list_1=[12,-7,5,64,-14]
print(negative(list_1))

#while

def neg(x):
    count=0
    while(count<len(x)):
        if(x[count]<0):
            print("Negative",x[count])
        count=count+1
list_2=[12,-7,5,64,-14]
print(neg(list_2))
