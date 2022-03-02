#Function

def sum_of_cube(x):
    sum_1=0
    for i in range(1,x+1):
        sum_1=sum_1+(i*i*i)
    return sum_1

no=int(input("Enter the number = "))
print(f"The number of {no} sum of cube is = ",sum_of_cube(no))

#forumala function

def sum_cube(x):
    return (x*(x+1)/2)**2

no=int(input("Enter the number = "))
print(f"The number of {no} sum of cube is = ",int(sum_cube(no)))
