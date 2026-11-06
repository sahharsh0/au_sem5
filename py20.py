''' series and dataframe'''
import pandas as pd
a=[1,2,3,4,5]
s=pd.Series(a)
s2=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
s3=pd.DataFrame({'A':[1,2,3,4,5], 'B':[6,7,8,9,10]})
print("Series:\n", s)
print("Series with custom index:\n", s2)
print("DataFrame:\n", s3)
dict={'Name':['Alice','Bob','Charlie','David','Eva'], 'Age':[25,30,35,40,45], 'City':['New York','Los Angeles','Chicago','Houston','Phoenix']}
print("DataFrame from dictionary:\n", pd.DataFrame(dict))
print("Series from dictionary:\n", pd.Series(dict))
print(s2.loc['a'])
print(s2.iloc[0])
print(s3.loc[0])