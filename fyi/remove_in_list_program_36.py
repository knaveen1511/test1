#for

def remov(x):
    for i in x:
        if(i%2==0):
            x.remove(i)
    return x
list_1=[11,5,17,18,23,50]
print(remov(list_1))
