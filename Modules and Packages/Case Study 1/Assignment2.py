# 2. Data of XYZ company is stored in sorted list. Write a program for searching
#     specific data from that list.
# Hint: Use if/elif to deal with conditions.

mylist = [1, 56, 'sa', 67, 'ga', 8, 're']
numberlist = []
alphalist = []
alphanum = []
print(len(mylist))
i = 0
while i < len(mylist):
    if mylist[i].isnumeric():
        numberlist.append(mylist[i])
    elif i.isalpha():
        alphalist.append(i)
    else:
        alphanum.append(i)
    i = +1

print(f'numbers :{numberlist}, alphabets:{alphalist}, alphanumeric: {alphanum}')
