#easy mehod
list_1=[12,10,5,6,52,36]
n=2
l=len(list_1)
list_1[:]=list_1[n:]+list_1[0:n]
print(list_1)
