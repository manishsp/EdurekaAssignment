# Please write a program which count and print the numbers of each character in a string input by console.Example: If
# the following string is given as input to the program:abcdefgabcThen, the output of the program should be:a,2c,2b,
# 2e,1d,1g,1f,1

s = 'abcdefgabc'
mydict = {}
for i in range(len(s)):
    # print(f"{s[i]},{s.count(s[i])}")
    mydict.update({s[i]: s.count(s[i])})

for j, k in mydict.items():
    print(f"{j},{k}")
