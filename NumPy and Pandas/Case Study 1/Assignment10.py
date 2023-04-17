# 10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
import numpy as np

arr = np.arange(11)
print(arr)
arr2 = np.negative(arr[2])
for x in range(len(arr)):
    if 3 < x < 9:
        arr[x] = np.negative(arr[x])

print("\n\nOutput with negeted value below\n", arr)
