def check(x,n):
    for i in list_1:
        if(n==i):
            return True
list_1=[1,2,3,4,5]
n=4
print(check(list_1,n))

#count method

def counting(x,n):
    count_1=x.count(n)
    if(count_1>0):
        return True
    else:
        return False
list_1=[11,12,13,14,15]
n=12
print(counting(list_1,n))
