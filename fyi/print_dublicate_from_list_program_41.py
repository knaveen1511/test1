def dublicate(x):
    count=0
    list_1=[]
    for i in x:
        if(x.count(i)>1):
            if(i !=list_1[0:] and list_1[0:]):
                print(i)
list_2=[10,20,30,30,15,26]
print(dublicate(list_2))

#while

list_1=[10,20,30,30,15,26]

list_2=[]

for a in list_1:
               n=list_1.count(a)
               if n>1 and list_2.count(a):
                   list_2.append(a)
            
print(list_2)            
               
               
