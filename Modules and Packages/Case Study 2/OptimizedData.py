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
newjoblist=set(job_list)
newjoblist.remove('job')
age_list.remove('age')
job_list=list(newjoblist)
# print(len(newjoblist)-1)
min_age=min(age_list)
max_age=max(age_list)
print(f'max:{max_age} min:{min_age}')

