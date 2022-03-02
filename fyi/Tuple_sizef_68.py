import sys

tuple_1=("A",1,"B",2,"C",3)
tuple_2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print(sys.getsizeof(tuple_1))
print(sys.getsizeof(tuple_2),"bytes")
print(sys.getsizeof(tuple3),"bytes")
