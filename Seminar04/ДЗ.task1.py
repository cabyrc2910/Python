#  Вычислить число c заданной точностью d
#  Пример:при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#################################################################

# from math import pi
# from decimal import Decimal
# import os
# os.system("cls")

# d = Decimal(input("Введите точность для числа π: "))
# print(f'\nЧисло π с заданной точностью {d} равно {str(pi)[:len(str(d))]}')

###################################################################

from math import pi

d = float(input('Введите точность: '))
count = 0
while d < 1:
    d *= 10
    count += 1
print(round(pi, count))