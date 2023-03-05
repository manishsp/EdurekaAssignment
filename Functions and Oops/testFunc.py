# list1 = [1,4,6,2,3,5,6,8,9]
# for x,y in enumerate(list1):
#     print(x, y)
# print(sum(list1))
# print(sorted(list1))
# print(list1)
#
# x=input("enter:")
# print(type(x))
# alpha=x.isalpha()
# numer=x.isalnum()
# upper=x.isupper()
#
# list1=[alpha,numer,upper]
# print(list1)
# print(any(list1))
# print(abs(float(x)))

# s="Sir to vote"
# print(list(reversed(s)))
# reversestr=str(reversed(s))
# print(reversestr)

# print(ord("	"))

#
# new=(lambda x:x*x)
# print(new(12))

class test():
    def mypublic(self):
        print("public method")

    def __myprivate(self):
        print("private method")


t = test()
t.mypublic()
t._test__myprivate()
