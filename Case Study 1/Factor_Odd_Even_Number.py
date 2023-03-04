# 1. Write a program which will find factors of given number and find whether the
# factor is even or odd

i = 1
factor = int(input("Please enter a number to find factor: "))
while i <= factor:
    if (factor % i) == 0:
        if i % 2 == 0:
            print(f"{i} is a factor of 10 and an even number.")
        else:
            print(f"{i} is a factor of 10 and an odd number.")

    i += 1
