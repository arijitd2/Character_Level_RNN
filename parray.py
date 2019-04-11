import numpy as np 
a = np.array([1, 0, 7])
b = np.zeros((3,8))
b[np.arange(3), a] = 1
print(b)

