# Напишите программу, которая принимает на вход число  N и выдаёт последовательность из N членов
# Пример: для N = 5:  1, -3, 9, -27, 81

import random
n = int(input('Введите произвольное целое число: '))
for i in range(n):
    print(random.randint(0,n))


import random
n = int(input('Введите произвольное целое число: '))
for _ in range(n):
    print(random.randint(-100,100))


from random import randint
n = int(input('Введите произвольное целое число: '))
for _ in range(n):
    print(randint(-100,100))


from random import *
n = int(input('Введите произвольное целое число: '))
for _ in range(n):
    print(randint(-100,100))


import random as rd
n = int(input('Введите произвольное целое число: '))
for _ in range(n):
    print(rd.randint(-100,100))


import random as rd
n = int(input('Введите произвольное целое число: '))
for _ in range(n):
    print(rd.randint(-100,100), end=' ')


N = int(input('Введите N: '))
z = 1
print(z, end=', ')
for i in range(N - 1):
    z = z * (-3)
    print(z, end=', ')