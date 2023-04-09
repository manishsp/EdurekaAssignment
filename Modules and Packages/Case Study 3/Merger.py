import struct

import Customer
import re

# fh=open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\Modules and Packages\\Case Study 3\\FairDealCustomerData.csv')
fh = open('/Users/MspDx/IdeaProjects/EdurekaAssignment/Modules and Packages/Case Study 3/FairDealCustomerData.csv')

# print(fh.read())
fullnamelist = []
blacklistvalue = []
customer_m = Customer.Customer()
for x in fh:
    x = re.sub('\s+', ' ', x)
    # x = x.strip('\n')
    mylist = str.split(x, ',')
    mylist[1]=str.strip(mylist[1])
    fullnamelist.append(str.strip(mylist[1]))
    blacklistvalue.append(mylist[2])
    splitname = re.split("\s", mylist[1])
    if len(splitname)==3:
        customer_m.setFname(splitname[1])
        customer_m.setTitle(splitname[0])
        customer_m.setLname(splitname[2])
    else:
        customer_m.setFname(splitname[1])
        customer_m.setTitle(splitname[0])
        customer_m.setLname("")

    print(customer_m.getTitle())
    print(customer_m.getFname())
    print(customer_m.getLname())
    # mydict = {"fullname": fullnamelist, "blacklist": blacklistvalue}

fh.close()
#
# print(splitname)
# print(customer_m.getTitle())
# print(customer_m.getFname())
# print(customer_m.getLname())