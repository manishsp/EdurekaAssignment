import Customer, re

fh=open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignments\\Modules and Packages\\Case Study 3\\FairDealCustomerData.csv')
# print(fh.read())
fullnamelist=[]
blacklistvalue=[]
for x in fh:
    x.rstrip('\n')
    # re.findall(r"\s+",x)

    mylist=str.rstrip.split(x,',')

    fullnamelist.append(mylist[1])
    blacklistvalue.append(mylist[2])
    mydict={"fullname":fullnamelist,"blacklist":blacklistvalue}
fh.close()
print(mydict)