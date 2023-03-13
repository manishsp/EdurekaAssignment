# 13.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
# sequence. Page 3 Module 4 – Working with Modules and Handling Exceptions Example: 0100,0011,1010,1001 Then the
# output should be: 1010
import MultiInput

newlist=MultiInput.MultiInput.input_data_with_comma(1)
for i in range(len(newlist)):
    if newlist[i]%5==0:
        print(newlist[i],end=",")
