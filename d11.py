import numpy as np
import pandas as pd
q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])

q_df.fillna('others')
pf=pd.get_dummies(q_df[['Sex']])
q_df=pd.concat([q_df,pf], axis=1)
print(q_df)
oso=q_df.fillna('others')
print(oso)
#用get_dummies叫好，因為是類別資料
ff=pd.get_dummies(oso[['Sex','Profession']])
oso=pd.concat([oso,ff], axis=1)
print(oso)