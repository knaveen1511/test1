#function(method 1)

def inter(a):
    b=len(a)
    #swapping
    temp=a[0]
    a[0]=a[b-1]
    a[b-1]=temp
    return a
list_1=[1,2,3]
print(inter(list_1))

#method 2

def change(a):
    b=len(a)
    a[0],a[-1]=a[-1],a[0]
    return a

list_1=[1,2,3,4,5]
print(change(list_1))

