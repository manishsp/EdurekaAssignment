# 13. Create a random array and swap two rows of an array.
import numpy as np

arr = np.random.randint(100, size=(2, 2))
print("original array\n", arr, "\n")
# long manual swap
arr2 = arr.copy()
arr[0, 0] = arr[1, 0]
arr[0, 1] = arr[1, 1]
arr[1, 0] = arr2[0, 0]
arr[1, 1] = arr2[0, 1]
arr3 = np.flipud(arr2)  # short inbuilt function to flip rows
print("output of long version \n", arr, "\n")
print("output of short inbuilt flipud() version \n", arr3, "\n")
