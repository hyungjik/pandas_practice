import pandas as pd

adf = pd.DataFrame({'x1': ['A', 'B', 'C'],
                   'x2': [1, 2, 3]})
print(adf)

bdf = pd.DataFrame({'x1': ['A', 'B', 'D'],
                    'x3': ['T', 'F', 'T']})
print(bdf)

# adf 를 기준으로 left  join (on은 key)
print(pd.merge(adf, bdf, how='left', on='x1'))
# bdf 를 기준으로 right join
print(pd.merge(adf, bdf, how='right', on='x1'))
# inner는 둘다 해당되는 값만
print(pd.merge(adf, bdf, how='inner', on='x1'))
# outer는 모든 값을
print(pd.merge(adf, bdf, how='outer', on='x1'))

# 필터링 조인
print(adf.x1.isin(bdf.x1))
print(adf[adf.x1.isin(bdf.x1)])
print(adf[~adf.x1.isin(bdf.x1)])


ydf = pd.DataFrame({'x1': ['A', 'B', 'C'],
                   'x2': [1, 2, 3]})

zdf = pd.DataFrame({'x1': ['B', 'C', 'D'],
                   'x2': [2, 3, 4]})

print(pd.merge(ydf, zdf))
print(pd.merge(ydf, zdf, how='outer'))
# indicator : merge를 어떻게 했는지 알려주는 컬럼 생성
print(pd.merge(ydf, zdf, how='outer', indicator=True))
print(pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"'))
print(pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge']))
