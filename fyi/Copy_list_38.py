#slicing

def clone(x,y):
    y[:]=x[:]
    return y
list_1=[1,2,3,4,5,6,7]
list_2=[]
print(list_1)
print(clone(list_1,list_2))
    
#copy
def cop(x,y):
    y.copy(x)
    return x
    
list_1=[1,2,3,4,5,6,7]
list_2=[]
print(list_1)
print(clone(list_1,list_2))
