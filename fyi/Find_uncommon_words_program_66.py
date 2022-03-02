a="Geeks for Geeks"
b="Learning from Geeks for Geeks"

a=a.split()
b=b.split()
print(a)
print(b)

c=set(b).symmetric_difference(set(a))
print(c)

