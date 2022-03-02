#second largest no

def second(x):
    x.sort(reverse=True)
    return x[1]
list_1=[12,23,345,45,76]
print(second(list_1))

