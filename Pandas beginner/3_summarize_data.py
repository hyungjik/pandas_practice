import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset("iris")
print(df.shape)
print(df.head())

# value_count ~행에서의 어떤값이 몇가지 들었는지
print(df['species'].value_counts())
print(pd.DataFrame(df['species'].value_counts()))

# 행의 갯수
print(len(df))  #  == df.shape[0]

# 유니크한 값의 갯수
print(df['species'].nunique())

# 전체 데이터 요약, include와 exclude로 형식 선택 가능
print(df.describe())
print(df.describe(include='all'))
print(df.describe(include=[np.object]))
print(df.describe(include=[np.number]))

'''
sum() : Sum values of each object.
count() : Count non-NA/null values of each object.
median() : Median value of each object.
quantile([0.25,0.75]) : Quantiles of each object.
apply(function) : Apply function to each object.
min() : Minimum value in each object.
max() : Maximum value in each object.
mean() : Mean value of each object.
var() : Variance of each object.
std() : Standard deviation of each object.
'''

# apply
print(df.apply(lambda x : x[1]))
# 세번째 글짜까지만 가져오기
print(df['species'].apply(lambda x : x[:3]))

# 뒤에서 세번째까지 문자 가져오는 함수
def smp(x):
    x = x[-3:]
    return x

# 외부에서 함수가져와서 호출
df['species_3'] = df['species'].apply(smp)
print(df)
