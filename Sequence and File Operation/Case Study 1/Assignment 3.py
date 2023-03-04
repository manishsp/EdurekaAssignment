# .A website requires a user to input username and password to register. Write a program to check the validity of
# password given by user. Following are the criteria for checking password:1. At least 1 letter between [a-z]2. At
# least 1 number between [0-9]1. At least 1 letter between [A-Z]3. At least 1 character from [$#@]4. Minimum length
# of transaction password: 65. Maximum length of transaction password: 12

def passwdCheck(x):
    numeric = x.isnumeric()
    alpha = x.isalpha()
    upper = x.isupper()
    if x in ('$', '#', '@'):
        specialChar = True
    else:
        specialChar = False

    return numeric + alpha + upper + specialChar


passwd = input("Enter password to validate: ")
passwdbooleanlist = []
for i in passwd:
    passwdbooleanlist.append(passwdCheck(i))
passboolcount = passwdbooleanlist.count(1) + passwdbooleanlist.count(2)
print(passwdbooleanlist)
print(passboolcount)
print(len(passwdbooleanlist))
if len(passwdbooleanlist) == passboolcount and passwdbooleanlist.count(2) >= 1:
    if 6 <= len(passwdbooleanlist) <= 12:
        print("Pass ok")
    else:
        print("Pass length is not correct!! it should be greater than 6 and can be maximum of 12 characters")
else:
    print("Pass not ok")
