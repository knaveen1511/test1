#def

def large(x):
    c=x[0]
    d=1
    while(c<x[d]):
        c=x[d]
        d+=1
    return c
list_2=[23,34,456,76,89,67,45]
print(large(list_2))

#max

list_2=[23,34,456,76,89,67,45]

print(max(list_2))

#sort

list_2=[23,34,456,76,89,67,45]
list_2.sort(reverse=True)
print(list_2[0])
