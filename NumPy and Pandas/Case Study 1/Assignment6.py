# 6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements greater than 5.
# 7. Create a numpy array having NaN (Not a Number) and print it. array([ nan, 1., 2., nan, 3., 4., 5.])
# Print the same array omitting all elements which are nan
# 8. Create a 10x10 array with random values and find the minimum and maximum values.
# 9. Create a random vector of size 30 and find the mean value.

import numpy as np

# arr=np.ndarray(shape=(3,4),strides=())
arr=np.reshape(np.arange(3*4),(3*4))
print(arr)