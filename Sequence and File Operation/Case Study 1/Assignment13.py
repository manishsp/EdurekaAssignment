# Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive.

# generate a list
# should limit to 5 elements
# in range 1 1000
#  should be divisible by 5 and 7
import random

list1 = []

while len(list1) < 5:
    i = random.randint(1, 1000)
    if i % 5 == 0 or i % 7 == 0:
        list1.append(i)

print (list1)
