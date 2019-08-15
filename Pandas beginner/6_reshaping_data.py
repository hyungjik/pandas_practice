import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('mpg')
print(df.shape)
print(df.head())
# mpg 기준으로 정렬
print(df.sort_values('mpg').head())
# 역순으로 정렬
print(df.sort_values('mpg', ascending=False).head())
# df에 저장을 해줘야 변경된다
print(df.rename(columns = {'model_year': 'year'}).head())
# 인덱스별로 정렬
print(df.sort_index().head())
# 인덱스를 새로 만들고 싶을때
print(df.reset_index().head())

# 특정행 삭제, 저장을 해야만 변경됨
print(df.drop(columns=['mpg', 'model_year']).head())
