from cryptography.fernet import Fernet


def refIDCheck(x):
    numeric = x.isnumeric()
    alpha = x.isalpha()
    if x in ('$', '#', '@', '%', '&', '*', '^', '!'):
        specialChar = True
    else:
        specialChar = False
    return numeric + alpha + specialChar


refID = input("Enter the 12 digit Reference ID: ")
refIDbooleanlist = []
for i in refID:
    refIDbooleanlist.append(refIDCheck(i))
refIDboolcount = refIDbooleanlist.count(1)

if len(refIDbooleanlist) == refIDboolcount:
    if len(refIDbooleanlist) == 12:
        print("Reference ID Validation is passed !!")
    else:
        print("Reference ID length is not correct!! it should be 12 digits")
        exit(8)
else:
    print("Reference ID Validation is Failed !! Only Numbers, Alphabets and Special Characters(@#$%^&*!) are allowed !!")
    exit(8)

message1 = refID
randomkey = Fernet.generate_key()
key1 = randomkey
fernet = Fernet(key1)
encodedmessage = fernet.encrypt(message1.encode())
myDict = {"message": message1, 'encKey': key1, "encoded-message": encodedmessage}
print(myDict)
print("Original Reference ID : ", message1)
print("Encrypted Reference ID : ", encodedmessage)


decryptSignal=input("Do you want to decrypt the above encoded message : Enter Y/N ? ")
if decryptSignal.upper()=="Y" or decryptSignal.upper()=="YES":
    decodedmessage = fernet.decrypt(encodedmessage).decode()
    print("Decrypted Reference ID : ", decodedmessage)
elif decryptSignal.upper()=="N" or decryptSignal.upper()=="NO":
    print("Okay, Exiting Program !!!")
else:
    print("Incorrect option entered.")


