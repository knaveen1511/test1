def even(s):
    string1=s.split(" ")
    for i in range(0,len(string1)):
        if((len(string1[i]))%2==0):
            print(string1[i])
s="This is a Python language"
print(even(s))
t = "i am muskan"
print(even(t))
