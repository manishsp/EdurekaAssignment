# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the
# i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡-Y-1. Example: Suppose the
# following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1,
# 2, 3, 4], [0, 2, 4, 6, 8]]

x, y = map(int, input("enter the value of x and y: ").split())
print(x, y)
mylist = []
for i in range(x):
    # print(i)
    mylist.append([])
    for j in range(y):
        # j=j-i
        mylist[i].append(j*(i-1))
        # print(mylist)
        j = +1
    i=+1
print(mylist)
