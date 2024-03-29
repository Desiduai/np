import numpy as np
import time as t

N = int(input('Введите кол-во столбцов: '))
M = int(input('Введите кол-во строк: '))

a = np.random.randint(-5,5,(N,M))
b = np.random.randint(-5,5,(N,M))
c = np.random.randint(-5,5,(int(input('Введите длину вектора: '))))
D = np.random.randint(-5,5,(N,N))
t.sleep(1)
print('\n',a)
print('\n',b)
print('\n',c)
print('\n',D)

def det():
    print('\nОпределитель матрицы D: ',np.linalg.det(D))

def count():
    k = np.count_nonzero(np.where(D < 0, D, None))
    k1 = np.count_nonzero(np.where(D > 0, D, None))
    print(k)
    print(k1)

    if (k > k1):
        d = np.where(D, D * (-1), None)
    print('\n', d)

def mult():
    K = int(input('Введите число на которое будент умножена матрица A: '))
    a1 = a.copy()
    a1 = np.multiply(a, K)
    print('\n', a1)

def some_strange_itterations():
    print('\n',np.add(a,b))
    print('\n',np.multiply(a,b))
    print('\n',a.dot(c))
    print('\n',a.transpose())
    print('\n',b.transpose())

def check():
    print('\n',np.transpose(a.transpose()) == a)
    print('\n',np.transpose(np.add(a,b)) == (np.transpose(a) + np.transpose(b)))
    print('\n',np.transpose(np.multiply(a,b)) == a.transpose() * b.transpose())

def raise_in_power():
    print('\n',np.power(a, 2))
    print('\n',np.power(a,3))
    print('\n',np.power(b, 2))
    print('\n',np.power(b,3))

def check_d():
    print(np.linalg.det(D))
    try:
        print('\n', np.linalg.inv(D))
    except BaseException:
        print('Oops. This matrix is singular')


print('\nВызов нужной вам функции...')
print('\nВыберите нужное: (1)Поиск определителя матрицы b. (2)Вынос минуса за "скобки". (3)Умножения матрицы A на число. (4)Умножения и сложения матрицы. (5)Проверка тождеств. (6)Возведение матриц в степень. (7)Нахождение обратной матрицы.')
R = int(input('Введите цифру: '))
if (R == 1):
    det()
elif (R == 2):
    count()
elif (R == 3):
    mult()
elif (R == 4):
    some_strange_itterations()
elif (R == 5):
    check()
elif (R == 6):
    raise_in_power()
elif (R == 7):
    check_d()
