import pandas as pd
import numpy as np

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
print(s1, s2)

print(pd.concat([s1,s2]))
print(pd.concat([s1,s2], ignore_index=True))
print(pd.concat([s1,s2], keys=['s1', 's2',], names=["Series name", 'row id']))

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                    columns=['letter', 'number'])
print(df1)

df2 = pd.DataFrame([['c', 3], ['d', 4]],
                    columns=['letter', 'number'])
print(df2)

print(pd.concat([df1, df2]))

df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                    columns=['letter', 'number', 'animal'])
print(df3)
print(pd.concat([df1, df3]))
# concat inner : 공통 column 만 join 하기
print(pd.concat([df1, df3], join="inner"))

df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']],
                    columns=['animal', 'name'])
print(df4)

df5 = pd.DataFrame([1], index=['a'])
df6 = pd.DataFrame([2], index=['a'])
print(df5)
print(df6)

# verify_integrity : index 중복이 있으면 에러발생
print(pd.concat([df5, df6], verify_integrity=True))
