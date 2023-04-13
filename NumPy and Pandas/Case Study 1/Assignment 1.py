# 1.# Extract data from the given SalaryGender CSV file and store the data from each
# # column in a separate NumPy array

import numpy as np
import pandas as pd

df = pd.read_csv('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignment\\NumPy and Pandas\\CSV\\SalaryGender.csv')

salary_arr = np.array(df["Salary"])
gender_arr = np.array(df["Gender"])
age_arr = np.array(df["Age"])
phd_arr = np.array(df["PhD"])

# print("*** Solution for 1 *** \n",salary_arr, "\n\n", gender_arr, "\n\n", age_arr, "\n\n", phd_arr, "\n\n")


# 2. Find:
# 1. The number of men with a PhD --assumed gender value as 1
# 2. The number of women with a PhD --assumed gender value as 0


df3 = df[(df['Gender'] == 1) & (df['PhD'] == 1)]  # assumed gender value as 1
df4 = df[(df['Gender'] == 0) & (df['PhD'] == 1)]  # assumed gender value as 0
womenwithphd = df4['Gender'].count()
menwithphd = df3['Gender'].count()

# print (f"*** Solution for 2 *** \nMen with PhD: {menwithphd} \nWomen with PhD: {womenwithphd} ")


# 3. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all
# people who don’t have a PhD from SalaryGender CSV file.

df5 = df[["Age","PhD"]]
print(df5)
for i in df5.index:
    if df5.loc[i,"PhD"] == 0:
        df5.drop(i, inplace=True)

print (f"*** Solution for 3 *** \n\n", df5)
# print(df5["Age"].count())
