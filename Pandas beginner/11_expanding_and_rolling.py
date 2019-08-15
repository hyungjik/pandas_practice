import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

s = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
print(s)

plt.figure()
# plt.plot(s)
# plt.show()

s = s.cumsum()
# plt.plot(s)
# plt.show()

r = s.rolling(window=60)
# print(r.mean())

# 이동평균을 구할때 쓴다. rolling
# s.plot(style='k--')
# r.mean().plot(style='k')
