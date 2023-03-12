# Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output. Hint: Use if else statements and functions.

def displayoptions():
    print("Welcome to ABC Bank online services !!!\nChoose one of the below options\n1. Cash Withdraw \n2. Cash Credit "
          "\n3. Change Password\n\n ")


def userinput():
    userchoice = int(input("Enter your input=====> "))
    if (userchoice >= 1 and userchoice <= 3):
        # return userchoice
        print("Enter your current password")
    else:
        yesno = input("No such option available, you want to try again ? Y/N")
        if yesno.upper() == 'Y':
            displayoptions()
        else:
            print("Thank you for using our online services !!!")


def cashwithdraw():
    accountbalance = 100
    amounttowithdraw = int(input("Enter the amount you want to withdraw: "))
    if amounttowithdraw > accountbalance:
        print("Insufficient Funds")
    else:
        accountbalance = accountbalance - amounttowithdraw
        print(f"Rs. {amounttowithdraw} withdrawn successfully, your current balance is {accountbalance}.")


def cashcredit():
    accountbalance = 100
    amounttocredit = int(input("Enter the amount you have credited: "))
    accountbalancenew = accountbalance + amounttocredit
    print(f"Rs. {amounttocredit} credited successfully, your updated balance is {accountbalancenew}.")


cashcredit()
