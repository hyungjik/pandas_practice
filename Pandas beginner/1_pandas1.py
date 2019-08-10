import pandas as pd
import numpy as np

# pandas cheet sheet 따라하기
# 2강
df = pd.DataFrame({"a": [4, 5, 6],
                   "b": [7, 8, 9],
                   "c": [10, 11, 12]},
                   index=[1, 2, 3])
print(df)
print(df['a'])
print(df.loc[3, "a"])
print(df.loc[[1,2],["a","b"]])


# 3강 중복 인덱스 생성
df = pd.DataFrame( [[4, 7, 10],
                    [5, 8, 11],
                    [6, 9, 12]],
                    index=[1, 2, 3],
                    columns=['a', 'b', 'c'])
print(df)

df = pd.DataFrame( {"a" : [4 ,5, 6],
                    "b" : [7, 8, 9],
                    "c" : [10, 11, 12]},
                    index = pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2)],
                                                        names=['n','v']))
print(df)

# 4강 subset observation (rows)
print(df[df.a < 7])
print(df[df.b > 7])
print(df.b > 7)
print(df[df['c'] > 7])  # 대소문자 구문하니까 잘 맞추자
print(df[df.c > 7])

df = pd.DataFrame( {"a" : [4 ,5, 6, 6, np.nan],
                    "b" : [7, 8, np.nan, 9, 9],
                    "c" : [10, 11, 12, np.nan, 12]},
                    index = pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2), ('e',3), ('e',4)],
                                                        names=['n','v']))
print(df)
# drop_duplicates는 중복된 행을 제거할때 사용한다.
print(df.drop_duplicates())  # 추가된 4번째 행 6,9,12,가 사라짐
df = df.drop_duplicates()  # inplace = True 를 활용할수있으나 이렇게 변수 저장을 권장함

# 5강
print(df["a"] != 7)
print(df[df["a"] != 7])

# df.columns.isin
print(df['a'].isin([5]))
print(df.a.isin([5]))
# null값 찾기
print(pd.isnull(df))

print(df['a'].isnull().sum()) # 특정행 null값의 개수

print(pd.notnull(df))
print(df.notnull().sum())

# &, |, ~, ^, df.any(), df.all()
# and, or not, xor, any, all

print(df.any())
print(~df.a.notnull())

# 6강
print(df.tail())
print(df.head())

# 특정비율(frac)로 df를 랜덤하게 샘플링함
print(df.sample(frac=0.5))
# n값을 지정
print(df.sample(n=3))

print(df.iloc[:2])
print(df.iloc[1:3])
print(df.iloc[3:])
print(df.iloc[-2:])

df = pd.DataFrame({'a': [1, 10, 8, 11, -1],
                   'b': list('abcde'),
                   'c': [1.0, 2.0, np.nan, 3.0, 4.0]})
# 숫자에서만 사용할 수 있는 nlargest
print(df.nlargest(3, 'a'))

print(df.nsmallest(1, 'a'))
