import numpy as np

a = np.random.randint(-5,5,5)
b = np.random.randint(-5,5,5)
print(a)
print(b)

x = np.where(a > 0, a, 0)
z = np.concatenate((b,x[np.nonzero(x)]), axis = None)

print(z)