#reversal algorithm

def reversal(x,start,end):
    while(start<end):
        temp=x[start]
    
        x[start]=x[end]
       
        x[end]=temp
      
        start=start+1
        end=end-1

def reversekey(y,d):
    n=len(y)
    reversal(y,0,d-1)
    reversal(y,d,n-1)
    reversal(y,0,n-1)
def printarr(z):
    for i in range (0,len(z)):
        print(z[i])

a=[1,2,3,4,5,6,7]
reversekey(a,2)
printarr(a)
