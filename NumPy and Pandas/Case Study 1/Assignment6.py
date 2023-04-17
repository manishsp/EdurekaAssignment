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

# 7. Create a numpy array having NaN (Not a Number) and print it. array([ nan, 1., 2., nan, 3., 4., 5.])



# Print the same array omitting all elements which are nan
# 8. Create a 10x10 array with random values and find the minimum and maximum values.
# 9. Create a random vector of size 30 and find the mean value.