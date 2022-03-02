#def function

def array(x):
    sum_1=0
    for i in x:
        sum_1=sum_1+i
    return(sum_1)

arr=[12,13,14,11]
print("the sum of array is = ",array(arr))

#sum method

def array(x):
    return(sum(x))

arr=[12,13,14,11]
print("the sum of array is = ",array(arr))
