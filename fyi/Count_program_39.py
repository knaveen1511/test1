#count
def coun(x,y):
    i=x.count(y)
    return i
list_1=[1,2,3,4,5,6,5,5]
c=5
print(coun(list_1,c))

#for

def cou(x,y):
    count=0
    for i in x:
        if(i==y):
            count=count+1
    return(count)
list_1=[1,2,3,4,5,6,5,5]
c=5
print(cou(list_1,c))    
