import re
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
print("The original list is : " + str(test_list))
temp = re.sub(r'[\[\]\(\), ]', '', str(test_list))
res = [int(ele) for ele in set(temp)]
print("The extracted digits : " + str(res))
