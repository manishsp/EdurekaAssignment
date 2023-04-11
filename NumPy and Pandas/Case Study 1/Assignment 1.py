# Extract data from the given SalaryGender CSV file and store the data from each
# column in a separate NumPy array

import numpy as np

arr=np.loadtxt('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignment\\NumPy and Pandas\\CSV\\SalaryGender.csv',delimiter=",",dtype=str)
print(arr)