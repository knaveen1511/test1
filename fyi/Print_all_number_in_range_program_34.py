#for
def positive_range(start,end):
    for i in range(start,end+1):
        if(i>=0):
            print("Positive",i)
start=-4
end=5
print(positive_range(start,end))
