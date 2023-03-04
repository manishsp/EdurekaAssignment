# Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have
# even indexes.
s = 'H1e2l3l4o5w6o7r8l9d'
i = 0
for i in range(len(s)):

    if s[i].isalpha():
        print(s[i], end="")
    else:
        continue
