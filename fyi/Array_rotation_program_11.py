#function method
def array(x,d):
    arr_1=[]
    for i in range(0,d):
        arr_1.append(x[i])
    i=0
    while(d<len(x)):
        x[i]=x[d]
        d=d+1
        i=i+1
    x[:]=x[:i]+arr_1
    return(x)
y=[1,2,3,4,5,6,7]
z=2
print(array(y,z))

#slicing method

def slicing(x,v,l):
    x[:]=x[v:l]+x[0:v]
    return(x)
y=[1,2,3,4,5,6,7]
z=len(y)
a=2
print(slicing(y,a,z))
