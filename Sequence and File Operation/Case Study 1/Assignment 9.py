# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
# duplicate values with original order reserved.

list1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
temp = set(list1)
list1 = (list(temp))
# print(list1[::-1])
# or
list1.sort(reverse=1)
print(list1)
