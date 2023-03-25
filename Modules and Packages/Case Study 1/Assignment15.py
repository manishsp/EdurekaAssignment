# 15. Give example of fsum and sum function of math library

# example is to find the total marks of a student

import math

marks_list = list(map(float, input("Please enter 4 subjects marks separated by space:").split(",")))

print(marks_list)
print(f"Total Marks via fsum: {math.fsum(marks_list)}")

print(f"Total Marks via sum: {sum(marks_list)}")
