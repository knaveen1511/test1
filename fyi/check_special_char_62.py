import re
str_1="Geeks For Geeks"
reject=re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if(reject.search(str_1)==None):
    print("Accepted")
else:
    print("Not Accepted")s
