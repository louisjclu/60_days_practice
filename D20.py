import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show
#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度, 若不給定值, 圖的周邊無文字
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)


#決定第二層框
plt.axes([.18, .18, .5, .5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([.18,.18,.5,.5])', ha = 'left', va = 'center', size = 16, alpha = .5)


#決定第三層框
plt.axes([.26, .26, .5, .5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([.26,.26,.5,.5])', ha = 'left', va = 'center', size = 16, alpha = .5)

#決定第四層框
plt.axes([.34, .34, .5, .5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([.34,.34,.5,.5])', ha = 'left', va = 'center', size = 16, alpha = .5)

plt.show()
#plt.show() #就是要這條東西==


# plt.figure()
# plt/subplot(2,1,1) --> 共二張圖，特定化版


# alpha 透明度


# plt.show()