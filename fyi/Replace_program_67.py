str_1="geeksforgeeks"

temp=str.maketrans("geek","abcd")
print(temp)

str_1=str_1.translate(temp)

print(str_1)
