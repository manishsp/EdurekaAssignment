# 6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3=arr.reshape(-1)
mylist=[]

for x in np.nditer(arr):
    if x>5:
        print(x," Greater than 5")
        mylist.append(True)
    else:
        print(x," Less than 5")
        mylist.append(False)
print(mylist)
arr2=arr3[mylist]
print(f'\nValues greater than 5:{arr2}')
