# Для натурального  n создать словарь индекс значение, состоящий из элементов последовательности 3n + 1
# Пример: для n = 6: [1:4, 2:7, 3:10, 4:13, 5:16, 6:19]

import numbers
from unittest import result


number = input('Введите число N: ')
result = []
for i in range(1, int(number)+ 1): #  Цикл из диапазона от 1 до 6
    elem = ([i, 3*i +1])
    result.append(elem)
print (dict(result))   # dict - переделывает данные в словарь


umber = input('Введите число N: ')
result = dict()
for i in range(1, int(number)+ 1):
    result[i] = 3*i+1
print (result)


N = int(input('Введите N: '))
for i in range(N):
    z = 3 * (i + 1) + 1
    print(z, end=', ')