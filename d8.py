import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']

sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']

weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]

rank_list = [8,1,5,4,7,6,2,3]

myopia_list = [True,True,False,False,True,True,False,False]
dt = np.dtype({'names':('Name', 'Sex', 'Weight', 'Rank','Myopia'), 'formats':((np.str_, 5), (np.str_, 5), np.float_, int, np.bool_)})
c=np.zeros(8, dtype=dt)
print(c)
print(c.dtype)


c['Name']=name_list
c['Sex']=sex_list
c['Weight']=weight_list
c['Rank']=rank_list
c['Myopia']=myopia_list
print(c)


avg_weight=np.mean(c['Weight'])
print('平均體重是：'+str(avg_weight)+' kg.')
male=c[c['Sex']=='boy']
print('男性平均體重是：'+str(np.mean(male['Weight']))+' kg.')
female=c[c['Sex']=='girl']
print('女性平均體重是：'+str(np.mean(female['Weight']))+' kg.')