"""i=[1,2,3,4,5,6,7,8,9]
n=4
l=len(i)
i_1=int(len(i)/4)
print(i_1)
print(l)

def four(x,n,y):
    count=0
    n_1=n
    for i in range(0,(int(len(x)/4))+1):
        list_i=[]
        try:
            for j in range(count,n):
                if(j<=len(x)):
                    list_i.append(x[j])
            print(list_i)
            count=count+n_1
            n=n+n_1
            
        except:
            print("Completed")
        
        
        
i=[1,2,3,4,5,6,7,8,9]
n=4
y=int(len(i)/4)
print(four(i,n,y))"""

l=[1,2,3,4,5,6,7,8,9]

n=4

for i in range(0,len(l),n):
    x=l[i:i +n]
    print(x)


