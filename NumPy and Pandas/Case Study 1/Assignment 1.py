# Extract data from the given SalaryGender CSV file and store the data from each
# column in a separate NumPy array

import numpy as np
import pandas as pd

df = pd.read_csv('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignment\\NumPy and Pandas\\CSV\\SalaryGender.csv')

salary_arr = np.array(df["Salary"])
gender_arr = np.array(df["Gender"])
age_arr = np.array(df["Age"])
phd_arr = np.array(df["PhD"])

print(salary_arr, "\n\n", gender_arr, "\n\n", age_arr, "\n\n", phd_arr, "\n\n")
