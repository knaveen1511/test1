#noram method

p=int(input("Enter The p= "))
t=int(input("Enter The t= "))
r=int(input("Enter The r= "))

print(f"Interest of princiipal {p} and time {t} and rate {r} is =",int(p*t*r/100))

#function method

def sinterest(p,t,r):
    print("The principal is = ",p)
    print("The principal is = ",t)
    print("The principal is = ",r)

    interest=int(p*t*r/100)

    return(interest)

x=10000
y=5
z=5

print("the interest is",sinterest(x,y,z))
