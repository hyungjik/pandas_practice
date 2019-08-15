import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')

print(df.groupby(by='origin'))
print(df.groupby(by='origin').size())

print(df['origin'].value_counts())

print(df.groupby(by='origin').min())

print(df.groupby(by='origin').mean())

print(df.groupby(by='origin')['cylinders'].mean())

print(df.groupby(['model_year', 'origin'])['cylinders'].mean())

df2 = pd.DataFrame([[4,7,10],
                    [5,8,11],
                    [6,9,12]],
                    index=[1,2,3],
                    columns=['a','b','c'])
print(df2)
# shift : 아래로 밀림
print(df2.shift(1))
print(df2['a'].shift(1))
# rank
print(df['model_year'].rank(method='max').value_counts())
print(df['model_year'].rank(pct=True).head())  # pct : 비율
print(df['model_year'].rank(method='first'))  # First : ?????

# cumsum : 누적합
print(df2.cumsum())

print(df2.cummax())  # 각 컬럼마다 row로 부터 max보다 작으면 그당시 max만 계속 출력
print(df2.cummin())  # 각 컬럼마다 row로 부터 min보다 크면 그당시 min만 계속 출력

print(df2.cumprod())  # row마다 누적곱
