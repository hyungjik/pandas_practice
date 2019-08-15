import pandas as pd
import numpy as np

df = pd.DataFrame({'A': range(1,11), 'B': np.random.randn(10)})
print('1\n', df)

print('2\n', df.assign(Area=lambda df: df['A']*df['B']))

print('3\n', df.assign(ln_A= lambda x: np.log(x.A)))

df["ln_A"] = np.log(df.A)
print('4\n', df)

# qcut 예제
print('5\n', pd.qcut(range(5), 3, labels=['good', 'medium', 'bad']))

print('6\n', pd.qcut(df.A, 3, labels=['good', 'medium', 'bad']))

print('7\n', pd.qcut(df.B, 3, labels=['good', 'medium', 'bad']))
# row에서 큰값
print('8\n', df.max(axis=1))
# column에서 큰값
print('9\n', df.max(axis=0))
# clip : 임계치를 지정함
print('10\n', df['A'].clip(lower=-10, upper=10))
# abs : 절대값
print('11\n', df['B'].abs())
