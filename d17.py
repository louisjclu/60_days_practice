import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
print(series)

#將所有轉為周資料
series2 = series.resample('W', convention='start',).asfreq()
print(series2)
#將周資料的值取平均
print('周資料的平均：')
print(series2.mean())