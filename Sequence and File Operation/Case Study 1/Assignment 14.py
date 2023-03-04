# Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).

n = int(input("Please enter a numeric value: "))
list1 = []
for i in range(1, n+1):
    x = (i / (i + 1))
    list1.append(x)
final=0
for j in range(0,len(list1)):
    final = final + list1[j]
print(f'Computed values in list: {list1}')
print(f'The sum of above listed values is {final}.')
