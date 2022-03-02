"""#clear method

def list_1(x):
    x.clear()
    return x
list_2=[1,2,3,4,5]
print(list_1(list_2))

#multiply 0
def lis(x):
    x*=0
    return x
list_1=[1,2,3,4,5]
print(lis(list_1))"""

#del method

list_10=[1,2,3,4,5]
print(list_10)
del list_10[:]
print(list_10)
