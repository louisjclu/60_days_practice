import pandas as pd
import numpy as np
score_df = pd.DataFrame([[1,50,80,70,'boy',1],[2,60,45,50,'boy',2],[3,98,43,55,'boy',1],[4,70,69,89,'boy',2],[5,56,79,60,'girl',1],[6,60,68,55,'girl',2],[7,45,70,77,'girl',1],[8,55,77,76,'girl',2],[9,25,57,60,'girl',1],[10,88,40,43,'girl',3],[11,25,60,45,'boy',3],[12,80,60,23,'boy',3],[13,20,90,66,'girl',3],[14,50,50,50,'girl',3],[15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])

#print(score_df)
df=score_df.melt(id_vars=['student_id','sex','class'])
print(df)
print('-------------')
df2=score_df.pivot_table(index=['student_id','sex','class'])
print(df2)
df3=df2.groupby('class').agg(['max', 'min'])
print(df3)

df4=df2.groupby('class').math_score.mean()
print(df4)

df5=df2.groupby('sex').chinese_score.mean()
print(df5)
print(' ')
print('兩組的差距為：') 
print(df5.iloc[1]-df5[0])