def count(x):
    count=0
    for i in x:
        count=count+1
    return(count)
list_1=[1,2,3,4,5]
print(count(list_1))

#import method

from operator import length_hint

list_1=[1,2,3,4,5]

print(length_hint(list_1))
