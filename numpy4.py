import numpy as np

N = int(input('Введите размерность матрицы: '))

a = np.random.randint(-2,5,(N,N))
print(a)

x = np.sum(np.where(a < 0, a, 0), axis = 0)

print('\n',x/N)