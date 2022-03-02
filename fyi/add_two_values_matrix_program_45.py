a= [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
b = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
x=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        x[i][j]=(a[i][j]+b[i][j])
print(x)
