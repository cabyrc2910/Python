# Найти корни квадратных уравнений.

from math import sqrt

a = int(input('Введите коэффициент а: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))
D = b**2 - 4 * a * c
if D > 0:
    x1 = (-b + sqrt(D)) / 2 * a
    x2 = (-b - sqrt(D)) / 2 * a
    print(f'Первый корень равен: {x1}')
    print(f'Второй корень равен: {x2}')
elif D == 0:
    x1 = -b / 2 * a
    print(f'Корень равен: {x1}')
else:
    print('Корней нет!')