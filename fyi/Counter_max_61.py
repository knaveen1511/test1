from collections import Counter

str1="GeeksforGeeks"

h=Counter(str1)
print(h)
g=max(h, key=h.get)
print(g)
