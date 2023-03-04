# 2. Data of XYZ company is stored in sorted list. Write a program for searching
#     specific data from that list.
# Hint: Use if/elif to deal with conditions.

# Section of code  to sort the list with both numeric and non-numeric

mylist = ['z', 1, 56, 'sa', 67, 'ga', 8, 're']

numberlist = []
alphalist = []

ctr = 0
for i in mylist:
    try:
        if i.isnumeric():
            numberlist.append(i)
        elif i.isalpha():
            alphalist.append(i)

        ctr += 1
        if ctr == len(mylist):
            break
        else:
            pass
    except AttributeError:
        numberlist.append(i)

print(f'numbers :{numberlist}, alphabets:{alphalist}')
mylist2 = sorted(numberlist) + sorted(alphalist)  # sort both the new lists separately and add it new list
print(mylist2)
# Section of search a specific data from new sorted list
searchinput = input("Enter the data to be searched in the company list\n ====> ")

try:
    if searchinput in mylist2:
        print(f"{searchinput} is found in the list")
    elif int(searchinput) in mylist2:
        print(f"{searchinput} is found in the list")
    else:
        print(f"{searchinput} is not found in the list")
except ValueError:
    print(f"{searchinput} is not found in the list")