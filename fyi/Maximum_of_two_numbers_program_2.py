#program 1(user input)

a=int(input("Enter The a= "))
b=int(input("Enter The b= "))
if(a>b):
    print(f"a is maximum {a}")
else:
    print(f"b is maximum {b}")

#program 2(max keyword)

def maxnumber(a,b):
    return(max(a,b))
x=12
y=13
print(f"the maximum number {x} and {y} = ",maxnumber(x,y))

#program 3(ternary operator)

a=54
b=87

print("the max number is = ",a if a>=b else b)
