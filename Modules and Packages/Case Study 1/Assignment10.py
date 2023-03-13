# 10.Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program:
# without,hello,bag,world Then, the output should be: bag,hello,without,world
# mannish,bitter,werk,thunder,zebra,cat

input_data = input("Enter the information to sort alphabetically:").split(",")
input_data.sort()
for i in range(len(input_data)):
    print(input_data[i], end=",")
