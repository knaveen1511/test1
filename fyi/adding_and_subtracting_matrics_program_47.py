a= [[1,2],[3,4]]
b= [[4,5],[6,7]]
c=[[0,0],[0,0]]
d=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
       c[i][j]=a[i][j]+b[i][j]
       d[i][j]=a[i][j]-b[i][j]

print(c)
print(d)

import numpy

a=numpy.array[[1,2],[3,4]]
b=numpy.array[[4,5],[6,7]]
print(numpy.add(a,b))
