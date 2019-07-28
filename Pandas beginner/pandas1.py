import pandas as pd

# pandas cheet sheet 따라하기
df = pd.DataFrame({"a": [4, 5, 6],
                   "b": [7, 8, 9],
                   "c": [10, 11, 12]}, index=[1, 2, 3])
print(df)
print(df['a'])
print(df.loc[3, "a"])
print(df.loc[[1,2],["a","b"]])
