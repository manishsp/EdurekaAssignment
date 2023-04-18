# 14. Create a random matrix and Compute a matrix rank.
import numpy as np

arr=np.arange(44).reshape(4,11)
print(arr)
print("\nMatrix Rank: ",np.linalg.matrix_rank(arr))
