def swap(x,pos1,pos2):
    x[pos1],x[pos2]=x[pos2],x[pos1]
    return x
list_1=[12,13,14,15]
pos1=0
pos2=2
print(swap(list_1,pos1,pos2))
