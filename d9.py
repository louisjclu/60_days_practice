import numpy as np
import pandas as pd
yes=pd.read_csv('/Users/louis/Desktop/boston.csv', usecols=['CHAS', 'NOX', 'RM'])
print(yes)
yes.to_excel('/Users/louis/Desktop/boston.xlsx')