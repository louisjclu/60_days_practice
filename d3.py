import numpy as np
x= float(input('請輸入微巴斯卡：'))
y= 20*np.log10(x/20)

print('您的分貝為：'+str(y)+'分貝')

a= float(input('請輸入分貝：'))
b= float(input('請輸入分貝：'))
c= 20*10**(a/20)/20*10**(b/20)
print('是'+str(c)+'倍')