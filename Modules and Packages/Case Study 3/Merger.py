import struct

import Customer, re

# fh=open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\Modules and Packages\\Case Study 3\\FairDealCustomerData.csv')
fh = open('/Users/MspDx/IdeaProjects/EdurekaAssignment/Modules and Packages/Case Study 3/FairDealCustomerData.csv')

# print(fh.read())
fullnamelist = []
blacklistvalue = []
for x in fh:
    x=re.sub('\s+',' ',x)
    # x = x.strip('\n')
    mylist = str.split(x, ',')
    fullnamelist.append(str.strip(mylist[1]))
    blacklistvalue.append(mylist[2])
    # mydict = {"fullname": fullnamelist, "blacklist": blacklistvalue}

fh.close()
print(f"fullname list length: {len(fullnamelist)} and blacklist list length: {len(blacklistvalue)}")

# print(fullnamelist[21])
# print(blacklistvalue[21])

# print(fullnamelist.index("Mr. William John"))
