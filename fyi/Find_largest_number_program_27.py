def larger(x,n):
    x.sort()
    list_2=[]
    for i in range (-1,-(n+1),-1):
        list_2.append(x[i])
    return(list_2)
list_1=[12,23,34,45,56,567,78,89]
y=int(input("how many large number you want to display: "))
print(f"{y} Largest no in the list",larger(list_1,y))
    
