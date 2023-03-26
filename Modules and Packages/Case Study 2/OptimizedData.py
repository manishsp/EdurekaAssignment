import re
fh=open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignment\\Modules and Packages\\Case Study 2\\bank-data.csv',"r")
# print(fh.read())
age_list=[]
job_list=[]
for x in fh:
    # print(x)
    mylist=str.split(x,",")
    age_list.append(mylist[0])
    job_list.append(mylist[1])

print(age_list)
print(job_list)

fh.close()