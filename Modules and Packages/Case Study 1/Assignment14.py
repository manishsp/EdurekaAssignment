# 14.Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

import MultiInput

to_compute = MultiInput.MultiInput.input_data_list("")
upper = 0
lower = 0
for i in range(len(to_compute)):
    if str(to_compute[i]).isupper() and str(to_compute[i]).isalpha():
        upper += 1
    elif str(to_compute[i]).islower() and str(to_compute[i]).isalpha():
        lower += 1
    else:
        pass

print(f"UPPER CASE {upper} \nLOWER CASE {lower}")
