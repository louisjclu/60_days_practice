import numpy as np
array1 = np.array(range(30))
array2 = np.array([2,3,5])

with open ('multi_array.npz', 'wb') as f:
    np.savez(f, array1=array1, array2=array2)

npzfile= np.load('multi_array.npz')
print(npzfile.files)
print(npzfile['array1'])
x=npzfile['array1']
y=npzfile['array2']
array3 = np.array([[4,5,6], [1,2,3]])

with open ('new_array.npz', 'wb') as f:
    np.savez(f, array1=x, array2=y, array3=array3)

OAO= np.load('new_array.npz')
print(OAO['array3'])
