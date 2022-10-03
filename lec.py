# # Файлы
# # a - открытие для добавления данных
# # r - открыти для чтения данных
# # w - открытие для записи данных
# # w+, r+ - открытие файла для записи и читать из него или наоборот

# # from turtle import color
# # from unittest.mock import patch

# with open('file.txt', 'a') as data: # меняем модификатор (a-запись,на r-чтение или w-перезапись)
#     data.write('line 1\n')
#     data.write('line 22\n')


# colors = ['red','green', 'blue']   # есть набор данных (список)
# data = open('file.txt', 'a')  # создаём текстовую переменную data, связываем её с текстовым файлом, указываем модификатор ('a', 'r' или 'w')
# # data.writelines(colors)     # разделителей не будет, в качестве аргумента передаём (colors)
# data.write('\nLine 2\n')      # чтобы что то дописать используем метод Write c переходом перед записью
# data.write('Line 3\n')        # переход после записи
# data.close()        # после работы с файлом его нужно закрыть (разорвать подключение фаловой переменной с файлом на диске)
# # если нажимать на включение программы, то каждый раз будет производиться дозапись(пересоздание) в file.txt (redgreenblue)


# patсh = 'file.txt'      # создаём путь к папке
# data = open(patсh, 'r')  # открываем в режиме чтения
# for line in data:        # далеее при помощи цикла пробежимся по файлу
#     print(line)           # считываем все строки
# data.close()          # после окончания чтения, разрываем связь

# exit()


# # Разделение программы на несколько файлов
from cgitb import reset
from tkinter import N
import hello        
print(hello.f(1))   # из одного скрипта используем функционал другого !!!!!!!

# import hello as h  # использование псевдонима другого файла
# print(h.f(1))


# # Значения по умолчанию для функции
# def new_string(symbol, count):  #  функция new_string принимает в качестве аргумента некоторый символ и число
#     return symbol * count        # возвращем строку умноженную на число
# print(new_string('!', 5)) #   !!!!!   (вызываем функцию передав в соответсвующее строку '!' и 2-й аргумент 5 )
# print(new_string('!'))    #   TypeError missing 1 required....


# def new_string(symbol, count = 3):   #  но если count = 3, по умолчанию значение явно не указывается
#     return symbol * count        
# print(new_string('!', 5)) #   !!!!!  
# print(new_string('!'))    #   !!!
# print(new_string(4))      #   12


# # Возможность передачи неограниченного количества аргументов
# def concatenatio(*params):
#     res: str = ""
#     # res: int = 0    # для работы с числами
#     for item in params:
#         res += item   # склеивание строк
#     return res

# print(concatenatio('a', 's', 'd', 'w'))    # asdw
# print(concatenatio('a', '1', 'd', '2'))    # a1d2
# # print(concatenatio(1, 2, 3, 4))    # TypeError: ...  , если не стоит (int) работа с числами


# #  Рекурсия
# def fib(n):           # Описываем функцию, указываем название (fib) и аргумент (N)
#     if n in [1, 2]:        # Прописываем логику выхода (если (n) содержится в списке состоящем из элементов 1 и 2)
#         return 1           # если попали в 1 элемент возвращаем (1), если во 2 то тоже (1)
#     else:
#         return fib(n-1)+ fib (n-2)    # возвращаем рекурсивный вызов

# list = []
# for e in range(1,10):   #  если требуется посмотреть
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34



# # Кортежи - неизменяемые списки
# t = ()
# print(type(t))    # tuple
# t = (1,)
# print(type(t))     # tuple
# t = (1)
# print(type(t))      # int
# t = (28, 9, 1990)
# print(type(t))      # tuple
# colors = ['red','green','blue']
# print(colors)      # ['red','green','blue']
# t = tuple(colors)
# print(t)           # ['red','green','blue']


# a = (3, 1, 41, 4)
# print(a)
# print(a [0]) # обращение к списку, получаем 3
# print(a [-2]) # обращение к списку, получаем 41
# # a[0] = 12  #  для кортежей это не работает, т.к список не изменяем

# t = tuple(['red','green','blue'])
# print(t[0])       # red
# print(t[2])       # blue
# # print(t[10])       # IndexError: 'tuple' index out of range
# print(t[-2])      # green
# # print(t[-200])     # IndexError: 'tuple' index out of range

# for e in t:
#     print(e)      # red green blue

# # t[0] = 'black'      # TypeError: 'tuple' object does not support item assignment


# a = (3, 4, 5)
# for item in a:
#     print(item)  # 3  4  5 (в столбик)

# t = tuple(['red','green','blue'])
# red, green, blue = t      # можно распоковать кортеж (t) в отдельные переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))   # r:red g:green b:blue



# # Словари - неупорядоченные коллекции произвольных обьектов с доступом по  ключу
# dictionary = {}
# dictionary = \
# {
#     'up':'↑',
#     'left':'←',
#     'down':'↓',
#     'right':'→',
# }

# print(dictionary['up'])  # изменения в словаре по ключу
# dictionary['up'] = 'up'
# print(dictionary['up'])    #  '↑','up'


# # print(dictionary)  #  {'up':'↑', 'left':'←','down':'↓','right':'→',}
# # print(dictionary['left'])  #  ←
# # типы ключей могут отличаться

# dictionary['left'] = '←'
# print(dictionary['left'])   # ←
# # print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']  # удаление элемента

# for item in dictionary:   # for (k, v) in dictionary.items():
#     print('{}: {}'.format(item,dictionary[item]))
# # up: ↑
# # left: ←
# # down: ↓
# # right: →


# for k in dictionary.keys():   # получаем ключи  'up','left','down','right'
#     print(k)

# for k in dictionary.values():  #  получаем значения  '↑','←','↓','→'
#     print(k)

# for v in dictionary:           # получаем ключи  'up','left','down','right'
#     print(v)

# for v in dictionary:            #  получаем значения  '↑','←','↓','→'
#     print(dictionary[v])



# #  Множества 
# colors = {'red', 'green','blue'}  
# print = (type(colors))      #  {'set'}  - тип данных множества
# print = (colors)            #  {'red', 'green','blue'}
# print = (type(colors))      #  {'set'}  - тип данных множества
# # exit
# colors.add('red')      #  добавить 'red', не добавится т.к. уже существует  
# print(colors)               #  {'red','green','blue'}
# colors.add('gray')     #  добавить 'gray'
# print(colors)               #  {'red','green','blue','gray'}
# colors.remove('red')   #  удалить 'red',
# print(colors)               #  {'green','blue','gray'}
# # colors.remove('red')          #  KeyError: 'red'
# colors.discard('red')       #  ok
# print(colors)               #  {'green','blue','gray'}
# colors.clear()         #  {}  - очистка множества
# print(colors)               #  set()  - тип данных множества


# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()         #  c = {1,2,3,5,8} - создание множества на основе имеющегося
# u = a.union(b)         # u = {1,2,3,5,8,13,21} - обьединение множеств
# i = a.intersection(b)  # i = {8,2,5} - пересечение
# dl = a.difference(a)    # dl = {1,3}
# dr = b.difference(a)    # dr = {13,21}

# q = a \
#     .union(b) \
#     .difference(a.inersection(b))
# # {1,21,3,13}

# s = frozenset(a)  # замороженое множество, методы добавления и удаления работать не будут


#  Списки
# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)    # 1 2 3 4 5     1 2 3 4 5   123 2 3 4 5   123 2 3 4 5


# list1[0] = 123 
# list2[1] = 333
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)     # 12 3 4 5    1 2 3 4 5   123 333 3 4 5   123 333 3 4 5


#     list1 = [1,2,3,4,5]

# print(len(list1))
# print(list1.pop()) 
# print(list1)             # 5 [1, 2, 3, 4] - метод (pop) извлекает последний стоящий элемент, остаётся новый список с учётом удалённого
# print(list1.pop())  
# print(list1)             # 4 [1, 2, 3]
# print(list1.pop())  
# print(list1)             # 4 [1, 2]

# print(list1.pop(2))      # удаление 2 элемента по индексу
# print(list1)             # [1, 2, 4, 5]

# print(list1.insert(2, 11)) # ставить на нужную позицию элемент 
# print(list1)               # [1, 2, 11, 3 , 4, 5]

# print(list1.append(11))     #  ставить элемент в конец списка 
# print(list1)                # [1, 2,  3 , 4, 5, 11]

