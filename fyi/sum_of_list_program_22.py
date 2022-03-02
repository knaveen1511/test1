#def
def add(x):
    count=0
    for i in x:
        count=count+i
    return(count)
list_1=[10,20,30,40]
print(add(list_1))

#sum

def add(x):
    count=sum(x)
    return(count)
list_1=[10,20,30,40]
print(add(list_1))

#while

list_1=[10,20,30,40]
count=0
total=0
while(count<len(list_1)):
    total=total+list_1[count]
    count=count+1
print(total)
