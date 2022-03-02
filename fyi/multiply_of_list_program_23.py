#def--for

def multi(x):
    count=1
    for i in x:
        count=count*i
    return count
list_1=[4,3,2,1]
print(multi(list_1))

#def-while

def multiply(x):
    total=1
    count=0
    while(count<len(x)):
        total=total*x[count]
        count+=1
    return total
list_1=[4,3,2,1]
print(multiply(list_1))

import math

list_1=[4,3,2,1]
c=math.prod(list_1)
print(c)
