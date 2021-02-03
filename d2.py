import numpy as np
array1 = np.array(range(30)) 
print(array1)
print(array1.reshape((5,6)))
print(np.where(array1%6==1))


b=array1.reshape((5,6), order='F')
print(b)
print(b[np.where(b%6==1)])