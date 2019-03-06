import numpy as np

a = np.random.randint(5,30,(10,10))
print(a)

n = a.min(axis = 1)
print(n)