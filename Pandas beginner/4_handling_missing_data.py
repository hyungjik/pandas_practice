import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5]],
                  columns=list('ABCD'))
# axis 0은 row 1은 column
# how에서 all은 모두 NaN인경우만
print(df.dropna(axis=1, how='all'))
print(df.dropna(axis=0, how='all'))
# how에서 any은 한개라도 NaN인경우만
print(df.dropna(axis=1, how='any'))

print(df.fillna(0))
values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
print(df.fillna(value=values))

print(df['D'].mean())
fill_na_value = df['D'].max()
print(df.fillna(fill_na_value))

# isnull 활용 NaN 갯수 확인
print(df.isnull().sum())
