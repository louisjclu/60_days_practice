import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show

x=np.arange(0,5,0.1)
y= np.sin(x)
z= np.cos(x)
#plt.plot(x,y,color='green', maker='x')
plt.plot(x,z, color='green', marker='.', linestyle='None')
plt.savefig('cos.png', dpi=300, format='png')

plt.show() #就是要這條東西==

