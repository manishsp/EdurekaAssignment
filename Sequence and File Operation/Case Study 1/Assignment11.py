# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [
# 12,24,35,70,88,120,155]
# import operator
# list1=[12,24,35,70,88,120,155]
# # print(list1.index(35))
# temp=operator.itemgetter(0,4,5)
# print(temp(list1))

list1 = [12, 24, 35, 70, 88, 120, 155]
list2 = []

list2 = [list1[i] for i in range(7) if i not in (0, 4, 5)]
print(list2)
