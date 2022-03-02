#function

def sum_of_squre(x):
    sum_1=0
    for i in range(1,x+1):
        sum_1=sum_1+(i*i)
    return(sum_1)
no=int(input("Enter the number = "))
print(f"The number of {no} sum of squre is = ",sum_of_squre(no))

#function 2    
def sum_squre(x):
    return (x*(x+1)*(2*x+1))//6
no=int(input("Enter the number = "))
print(f"The number of {no} sum of squre is = ",sum_squre(no))
