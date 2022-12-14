# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. d = √(xb - xa)2 + (yb - ya)2
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

##########################################################

# from math import sqrt
# import math
# from unittest import result
# x1 = int(input('Введите координату первой точки X: '))
# y1 = int(input('Введите координату первой точки Y: '))
# x2 = int(input('Введите координату второй точки X: '))
# y2 = int(input('Введите координату второй точки Y: '))
# # d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
# d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print('Расстояние между точками равно: ', round(d, 2))

#############################################################

import math
print('Введите координату первой точки')
xa = int(input('Введите координату точки X: '))           # Введите координату точки X: 1
ya = int(input('Введите координату точки Y: '))
print('Введите координату второй точки')
xb = int(input('Введите координату точки X: '))
yb = int(input('Введите координату точки Y: '))
result = math.sqrt((xb - xa)**2 + (yb - ya)**2)
result = round(result, 2)
print('Расстояние между точками равно:', round(result, 2))   # Расстояние между точками равно: 0.00