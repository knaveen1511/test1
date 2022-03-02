def odd(x):
    count=0
    list_2=[]
    while(count<len(x)):
        if(x[count]%2!=0):
            list_2.append(x[count])
        count=count+1
    return(list_2)
list_1=[2,7,5,64,14]
print(odd(list_1))
