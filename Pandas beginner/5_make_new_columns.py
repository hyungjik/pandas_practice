import pandas as pd
import numpy as np

df = pd.DataFrame({'A': range(1,11), 'B': np.random.randn(10)})
print(df)

df.assign(Area=lambda df: df['A']*df['B'])
