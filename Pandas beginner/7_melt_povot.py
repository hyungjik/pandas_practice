import pandas as pd

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
print(df)

# melt 함수 : column을 row로 옮기기
print(pd.melt(df, id_vars=['A'], value_vars=['B']))

print(pd.melt(df, id_vars=['A'], value_vars=['B', 'C']))

print(pd.melt(df, value_vars=['A', 'B', 'C']).rename(columns={'variable':'var', 'value':'val'}))

# pivot :
df2 = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6]})
print(df2)

print(df2.pivot(index='foo', columns='bar', values='baz'))
print(df2.pivot(index='foo', columns='bar', values='baz').reset_index())

# melt 로 다시 원복하기...
df3 = df2.pivot(index='foo', columns='bar', values='baz').reset_index()

print(df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar']))
