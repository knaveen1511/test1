

#interchange last to first--->5

def interchange(x):
    x=x[-1::-1]
    print(x)
    return()
y=[12,34,56,67]
interchange(y)
    
#len method--->6
def length(x):
    count=0
    for i in x:
        count+=1
    print(count)
    return()
y=[12,34,56,78,90,23,45,67]
length(y)

       


#multiplication method to list----8

list_1=[1,2,3,4]
count=0
total=1
while(count<len(list_1)):
    total=0+(total*list_1[count])
    count=count+1
print(f"The mulitiplication of{list_1} = ",total)

#find smallest No---->9(sort method)------------>9

def small(a):
    a.sort()
    print(a[0])
x=[11,34,76,45,89,3]
small(x)

#find largest no in list--->10

list_1=[]

no=int(input("Enter the no = "))
for i in range(0,no):
    user=int(input("Enter the List = "))
    list_1.append(user)
list_1.sort(reverse=True)
print(list_1[0])

#second large no--------------->11

list_1=[]

no=int(input("Enter the no = "))
for i in range(0,no):
    user=int(input("Enter the List = "))
    list_1.append(user)
list_1.sort(reverse=True)
print(list_1[1])

#even list--------------->12

list_1=[12,65,34,89]
list_2=[]
for i in list_1:
    if(i%2==0):
        list_2.append(i)

print("Even no is = ",list_2)
    
#add--------------------------->13
num=int(input("Enter the no = "))
list_1=[]
while(num>0):
    i=int(input("Enter the add no = "))
    list_1.append(i)
    num=num-1
for i in list_1:
    if(i%2==0):
        pass
    else:
        print(i,end=" ")
#range even------------------------>14

a=int(input("enter the a = "))
b=int(input("enter the a = "))

for i in range(a,1+b):
    if(i%2==0):
        print(i,end=" ")
#negative numbers----------------------->15

list_1=[-1,2,3,6,8,-8]
count=0
while(count<len(list_1)):
    if(list_1[count]<0):
        print(list_1[count])
    count+=1
neg=[i for i in list_1 if i<0]
print(*neg)

#positive no--------------->16

list_1=[-1,-56,54,-4,-3,4]
pos=[i for i in list_1 if i>0]
print(*pos)

#range positive----------->17

a=int(input("Enter the a = "))
b=int(input("Enter the a = "))

for i in range(a,1+b):
    if(i>=0):
        print(i)
#Ascii value--------------->18

a=input("Enter the string: ")
print(ord(a))

#sum of square--------->19
num=int(input("Enter the number = "))
num_list=[]
total=0
count=0
for i in range(1,num+1):
    i=i**2
    num_list.append(i)
    i=i-1
while(count<len(num_list)):
    total=total+num_list[count]
    count+=1
print("the sum of sequre is = ",total)

#sum of cube------------->20

def cube(x):
    total=0
    for i in range(1,x+1):
        i=i**3
        total=total+i
    print("sum o cube no is",total)
y=5
cube(y)

#python reverse list---------->21

list_1=[10,11,12,13,14,15]

print(list_1[::-1])

#python copy--------->22

list_1=[4,8,12,16,20,24,28]
list_2=[]
list_2=list_1.copy()
print(list_1)
print(list_2)

#count method_-------------->23
list_1=[3,6,9,12,15,18,20,6]
x=int(input("Enter the number = "))
count=0
for i in list_1:
    if(i==x):
        count=count+1
print("the count no is = ",count)

#string palindrome--------->24

string_1=input("Enter the string: ")

if(string_1==string_1[::-1]):
    print("it is palindromr")
else:
    print("it is not palindrome")
#add two number matrix---->25

list_1=[12,34,56,78,90]
list_2=[98,76,54,32,10]
list_3=[]

for i in range (0,len(list_1)):
        list_3.append(list_1[i]+list_2[i])
print(list_3)

#multiply two number matrix---->26#------------------#

x=[[1,7,3],[3,5,6],[6,8,9]]
y=[[1,1,1,2],[6,7,3,0],[4,5,9,1]]
count=len(x)
z=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range (0,len(x)):
    for j in range(0,(len(y[0]))):
        for k in range(0,len(y)):
                       z[i][j]+=x[i][k]*j[i][k]
        print(z)
#negative no in range----->27

a=int(input("Enter the No A = "))
b=int(input("Enter the No B = "))

for i in range(a,b):
    if(i<0):
        print("negative no",i)
#size of tuple---->28

tuple_1=(1,2,3,4,5,"hi","Hello","bye")
print(tuple_1.__sizeof__(),"bytes")
tuple_2=(1,2,3,4,5,"Hi","How are you")
print(tuple_2.__sizeof__(),"bytes")

#list of tuple into list--->29

list_1=[1,2,3]
list_2=[]
for i in range(len(list_1)):
    tuple_1=(list_1[i],list_1[i]**3)
    list_2.append(tuple_1)
print(list_2)"""

#adding set and list

list_1=[1,2,3]
tuple_1=4,5

list_1 +=tuple_1
print("adding tuple and list",list_1)

    
