# 5.Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.
p=input("Enter a number to determine if it Palindrome: ")
# s=p[::-1]
if p==p[::-1]:
    print(f"Given input {p} is Palindrome")
else:
    print(f"Given input {p} is not a Palindrome")