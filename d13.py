import numpy as np
import pandas as pd
df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)
})

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)
})
print(df1)
print(df2)


df3= pd.merge(df1,df2, how='outer',on='fruit')
print(df3)

#2. 承上題，請問為什麼依照 merge 合併後有些資料不見了
print('當使用merge的時候，預設為 how = "inner"，資料內容相同的就會被合併，重複的資料就會被消除')
#3. [簡答題] 承上題，請問為什麼依照 index 合併會發生錯誤？請用程式解決。
print('因為兩個 Data Frame 有重複的欄位名稱，將重複的欄位分別命名成新欄位即可')
print(df1.join( df2, lsuffix='_df1', rsuffix='_df2' ))