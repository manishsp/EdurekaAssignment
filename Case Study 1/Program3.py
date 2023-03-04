# Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a
# number is an even number. The numbers obtained should be printed in a comma separated sequence on a single
# line.Hint: In case of input data being supplied to the question, it should be assumed to be a console input.Divide
# each digit with 2 and verify is it even or not.
start_range = int(input("Provide start range: "))
end_range = int(input("Provide end range: "))

if end_range > start_range:
    for i in range(start_range, end_range):
        l = list(str(i))
        even_list = []
        for j in l:
            check_even = int(j)
            if check_even != 0 and check_even % 2 == 0:
                even_list.append(str(check_even))
        if l == even_list:
            for k in even_list:
                print(k, end=",")
else:
    print("End Range can't be less than start range!!")
