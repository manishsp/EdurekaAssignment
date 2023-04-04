import re

fh = open('C:\\Users\\pmani\\IdeaProjects\\EdurekaAssignment\\Modules and Packages\\Case Study 2\\bank-data.csv', "r")
# print(fh.read())
age_list = []
job_list = []
for x in fh:
    # print(x)
    mylist = str.split(x, ",")
    age_list.append(mylist[0])
    job_list.append(mylist[1])

fh.close()
newjoblist = set(job_list)
newjoblist.remove('job')
print(f'Unique jobs are {newjoblist}')
age_list.remove('age')
job_list = list(newjoblist)

eligible_client = ['admin.', 'self-employed', 'services', 'technician']
while x != 'END':

    check_profession = input('Please enter the profession to check eligibility: ')
    if check_profession.upper() != 'END':
        if check_profession.lower() in newjoblist:
            print(f"{check_profession} profession is in list ")
            if check_profession.lower() in eligible_client:
                print(f"Client is eligible for loan")
            else:
                print(f"Client is not eligible for loan")
        else:
            print(f"{check_profession} profession is not in list ")
    else:
        x = 'END'

age_dict = {"Minimum age": min(age_list), "Maximum age": max(age_list)}
print(age_dict)
