import numpy as np

a = np.array([[2,3],[1,0],[-1,3]])
b = np.array([[2,0,1],[1,-2,2],[5,0,3]])
print('\n',a)
print('\n',b)
x = np.multiply(a,2)
y = b.dot(a)

print('\n', x-y)