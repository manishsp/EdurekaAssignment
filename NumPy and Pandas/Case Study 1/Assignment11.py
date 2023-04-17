# 11. Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.
import numpy as np

arr=np.random.randint(100,size=(3,3))
print(arr)
arr2=np.sort(arr,axis=0)
print("\n\nOutput with vertical sorted value below\n", arr2)