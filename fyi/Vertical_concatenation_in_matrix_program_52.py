from itertools import zip_longest

list_1=[["gfg","good"],["is","for"]]

list_2=["".join(i) for i in zip_longest(*list_1,fillvalue="")]

print(list_2)
