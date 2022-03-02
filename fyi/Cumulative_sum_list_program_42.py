def cumulative(x):
    count=0
    add=1
    while(count<len(x) and add<len(x)):
        x[add]=x[count]+x[add]
        count=count+1
        add=add+1
    return(x)
list_1=[10,20,30,40,50]
list_2=[4,10,15,18,20]
print(cumulative(list_1))
print(cumulative(list_2))
