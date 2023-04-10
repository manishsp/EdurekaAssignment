import Customer
import re


class CustomerNotAllowedException(Exception):
    def __init__(self, value):
        self.value = self
        print(f'Customer: {self.value} is blacklisted and not allowed')


fh = open(
    'C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\Modules and Packages\\Case Study 3\\FairDealCustomerData.csv')
# fh = open('/Users/MspDx/IdeaProjects/EdurekaAssignment/Modules and Packages/Case Study 3/FairDealCustomerData.csv')

# print(fh.read())
fullnamelist = []
blacklistvalue = []
customer_m = Customer.Customer()
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


    def createOrder(y, z):
        try:
            if z == 0:
                print(f"Customer: {y} is not blacklisted")
            else:
                raise CustomerNotAllowedException(y)
        except CustomerNotAllowedException as e:
            # print(e.args)
            pass


    createOrder(customer_m.getFname(), customer_m.isblacklisted)

fh.close()
