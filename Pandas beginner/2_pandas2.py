import pandas as pd
import numpy as np
import seaborn as sns

# 7강
df = sns.load_dataset("iris")
print(df.head())

# 특정컬럼만 가져오기
columns = ['sepal_length', 'sepal_width', 'species']
print(df[columns])

#
print(df['sepal_width'])  # or df.sepal_width

# 정규표현식으로 _가 포함된 열 가져오기
print(df.filter(regex='_').head())
# length로 끝나는 열 가져오기
print(df.filter(regex='length$').head())
# 특정문자로 시작하는것 가져오기
print(df.filter(regex='^sepal').head())
# species 가 아닌것 출력
print(df.filter(regex='^(?!species$).*').head())
# 행과 열로 지정해서 가져옴
print(df.loc[:5, 'sepal_width':'petal_width'])
# iloc는 5포함안함 loc은 포함
print(df.iloc[:5, [1,2,4]])
# 행과 열 지정
print(df.loc[df['sepal_length'] > 5, ['sepal_length', 'sepal_width']].head())
