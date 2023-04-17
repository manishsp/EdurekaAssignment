# 9. Create a random vector of size 30 and find the mean value.

import numpy as np

arr=np.random.randint(100, size=30)
print(arr)
print("Mean value of above vector: ",np.mean(arr))