# 12. Create a four dimensions array get sum over the last two axis at once.
import numpy as np

arr = np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[8,9],[10,11]],[[12,13],[14,15]]]], ndmin=4)
print("4 dimensional array\n*************\n",arr,"\n*************")
print("Last 2 axis\n*************\n",arr[1,1],"\n*************")
arr2=np.sum(arr[1,1])
print("Sum of last 2 axis",arr2)
