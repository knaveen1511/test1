#largest no

def largest(x):
    return max(x)
arr=[11,14,23,67,89]
print("the Largest no of array is = ",largest(arr))

#for condition

def larger(x,n):
    max_1=x[0]
    for i in range(1,n):
        if(x[i]>max_1):
            max_1=x[i]
    return(max_1)
        
arr=[11,14,89,67,23]
n=len(arr)
print("the Largest no of array is = ",larger(arr,n))
