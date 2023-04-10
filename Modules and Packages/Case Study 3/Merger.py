import Order

import Customer
import re


class CustomerNotAllowedException(Exception):
    def __init__(self,value):
        self.value=self


# fh=open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\Modules and Packages\\Case Study 3\\FairDealCustomerData.csv')
fh = open('/Users/MspDx/IdeaProjects/EdurekaAssignment/Modules and Packages/Case Study 3/FairDealCustomerData.csv')

# print(fh.read())
fullnamelist = []
blacklistvalue = []
customer_m = Customer.Customer()
# ord1= Order.Order()
for x in fh:
    x = re.sub('\s+', ' ', x)
    mylist = str.split(x, ',')
    mylist[1] = str.strip(mylist[1])
    fullnamelist.append(str.strip(mylist[1]))
    blacklistvalue.append(mylist[2])
    splitname = re.split("\s", mylist[1])
    if len(splitname) == 3:
        customer_m.setFname(splitname[1])
        customer_m.setTitle(splitname[0])
        customer_m.setLname(splitname[2])
    else:
        customer_m.setFname(splitname[1])
        customer_m.setTitle(splitname[0])
        customer_m.setLname("")
    customer_m.setIsblacklisted(int(mylist[2]))

    # print(f"{customer_m.getFname()} {customer_m.getLname()}: {customer_m.isblacklisted}")

    try:
        if customer_m.isblacklisted == 0:
            print(f"Customer: {customer_m.getFname()} {customer_m.getLname()}is not blacklisted")
        else:
            raise CustomerNotAllowedException("Exception")
    except CustomerNotAllowedException:
        print(f"Customer: {customer_m.getFname()} {customer_m.getLname()} is blacklisted and not allowed")

Order.Order.createOrder("William",1,"XXXX","yyy")

    # def createOrder(y,z):
    #     if z==1:
    #         raise CustomerNotAllowedException
    #     else:
    #         print(f"order created for {y}")
    # createOrder(customer_m.getFname(),customer_m.isblacklisted)

fh.close()

Order.Order.createOrder()