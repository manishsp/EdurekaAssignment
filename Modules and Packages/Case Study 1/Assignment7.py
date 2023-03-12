# 7. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Hint: Suppose the following input is supplied to the program:
# 8
# Then, the output should be: 40320

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


userinput = int(input("Enter number to find its factorial: "))
print(f"Factorial of number {userinput} is {factorial(userinput)}")
