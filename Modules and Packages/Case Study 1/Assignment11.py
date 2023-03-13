# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the
# sentence capitalized. Suppose the following input is supplied to the program: Hello world \n Practice makes perfect
# Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT


loop_info = int(input("How many number of line you wish to capitalize:"))

input_data = []
for i in range(loop_info):
    try:
        line = input("Enter your input: ")
    except:
        pass
    input_data.append(line.upper())

print("\n\n ---- Capitalized Output----\n ")
for i in range(len(input_data)):
    print(input_data[i], end="\n")
