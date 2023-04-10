# import numpy as np
import pandas as pd

# a=np.array([1, 2, 3, 4])
# a=np.array([[1, 2], [3, 4],[5,6]])
# list1=[1,2,3,4]
# a=np.array(list1)
# a=np.arange(20)
# a=np.zeros((12,3),dtype=int)
# a=np.linspace(0,10,8)
# a = np.zeros(8)
# b = a.reshape((2, 2, 2))
# b=slice(1,10,2)
# print(a)
# print(b)

# print(a[b])

# new=pd.Series()
# new=pd.Series([2,20,2])
# mydict={"a":1,"b":2,"c":3}
# new=pd.Series(mydict)
# print(new[::-1])
# listx=[1,23,45,23,45,56]
# mydict=[{"a":1,"b":2,"c":3},{"a":33,"b":22}]
# new=pd.DataFrame(mydict,index=["first","second"])
data={"one":pd.Series([1,2,3,4], index=['a','b','c','d']),
      "two":pd.Series([5,6,7], index=['a','b','c'])}
new=pd.DataFrame(data)
new['three']=pd.Series([10,23,45],index=['a','b','d'])
# del new['one']
# new.pop('two')

print(new)
print(new.loc['b'])
print(new.iloc[3])