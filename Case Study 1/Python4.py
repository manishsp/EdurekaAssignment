# 4.Write a program that accepts a sentence and calculate the number
# of letters and digits.Suppose if the entered string is: Python0325
# Then the output will be:LETTERS: 6DIGITS:4Hint: Use built-in functions of string

s = input("Please enter a sentence to calculate no. of letters and digits:")

letter=0
digits=0
for i in s:

    if i.isnumeric() is True:
        digits += 1
    elif i.isalpha() is True:
        letter += 1
print (f"LETTERS: {letter} and DIGITS: {digits}")