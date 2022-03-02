#simple method

p=int(input("Enter the Principal = "))
t=int(input("Enter the time = "))
r=float(input("Enter the rate = "))

amount=p*((1+r/100)**t)
cinterest=amount-p
print("Compound interest = ",cinterest)

#func method

def cinterest(p,t,r):
    print("the principal is = ",p)
    print("the time is = ",t)
    print("the rate is = ",r)
    amount=p*((1+r/100)**t)
    cinter=amount-p
    return cinter

x=1200
y=2
z=5.4
print("Compound interest = ",cinterest(x,y,z))
