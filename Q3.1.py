# На вход программе подаются 2 целых числа a и b каждое на отдельной строке.
# Программа должна вывести результаты математических операций в соответствии с условием задачи

import math
a = int(input('Введите а: '))
b = int(input('Введите b: '))

print (a+b)  # сумму чисел a и b
print (a-b)    # разность чисел a и b
print (a*b)   # произведение чисел a и b
print (a**b)   # возведение  числа a в степень b
print (a/b)     # частное (деление) чисел a и b; - QUOTIENT
print (a//b)      # целую часть от деления числа a на b
print (a%b)     # остаток от деления от числа a н аb
print (math.sqrt(b))   # корень квадратный  из b. Формат входных данных