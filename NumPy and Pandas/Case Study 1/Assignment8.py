# 8. Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

arr = np.random.randint(1000, size=(10, 10))
print(arr)
print("Minimum value in array is ",np.min(arr)," and maximum value is ",np.max(arr))