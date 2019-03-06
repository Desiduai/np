import numpy as np

a = np.random.randint(1,5,10)
print(a)

x = np.where(a%2 != 0, a, a*2)
z = np.where(a%2 == 0, a, 0)

print(x)
print(z)