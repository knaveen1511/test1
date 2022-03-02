def string_k(k,str_1):
    string=[]
    text=str_1.split(" ")
    for i in text:
       if len(i)>k:
           string.append(i)
    return string
k=3
str_1="geek for geeks"
print(string_k(k,str_1))
