#for loop
def positive(x):
    for i in x:
        if(i>0):
            print("Positive numbers",i)
list_1=[12,-7,5,64,-14]
print(positive(list_1))

#while

def pos(x):
    count=0
    while(count<len(x)):
        if(x[count]>0):
            print("Positive numbers",x[count])
        count=count+1
            
list_2=[12,-7,5,64,-14]
print(pos(list_2))
