# Задайте 2 числа. Напишите программу, которая находит наименьшее общее кратное этих двух чисел.

########################################################

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# nok = max(a, b)
# while not (nok%a == 0 and nok%b == 0):

#     nok += max(a, b)
# print(nok)

#########################################################  

a, b = 6, 8
nok = max(a, b)
while not(nok%a == 0 and nok%b == 0):  # while nok%a !+0 or nok%b !=0: 
    nok += max(a, b)
print(nok)  #  24


# a, b = 1000, 1001
# nok = max(a, b)
# # while nok % a != 0 or nok % b != 0:
# while not (nok % a == 0 and nok % b == 0):
#     nok += max(a, b)
# print(nok)
  