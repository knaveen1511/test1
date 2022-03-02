str1='abcdef'
str2='defghia'
count=0
for i in str1:
    if i in str2:
        count+=1
print(count)

str_1='aabcddekll12@'
str_2='bb22ll@55k'
set_1=set(str_1)
set_2=set(str_2)
set_3=set()
for i in set_1:
    if i in set_2:
        set_3.add(i)
print(set_3)

set_4=set_2.intersection(set_1)
print(set_4)
