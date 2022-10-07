# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

##################################################################

my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [(num % 1) for num in my_list if isinstance(num, float)]
# type(num) == float
print (new_list)
max_num = max(new_list)
min_num = min(new_list)
print(max_num - min_num)

################################################################

# from itertools import count
# import os
# from unittest import result
# os.system("cls")
# source_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]
# print(f'{source_list} = > {max(new_list) - min(new_list)}')

##################################################################

# import os
# os.system("cls")
# source_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = []
# for i in source_list:
#     if i % 1 != 0:
#         new_list.append(round(i % 1, 2))
# print(f'{source_list} = > {max(new_list) - min(new_list)}')

####################################################################

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# max = my_list[0] % 1 * 100
# min = my_list[0] % 1 * 100
# j = int
# for i in my_list:
#     j = i % 1 * 100
#     if j > 0:
#         if j > max: max = j
#         if j < min: min = j
# result = (max - min) / 100
# print(round(result, 2))

####################################################################

# source_list = [1.1, 1.2, 3.1, 5, 10.01]
# new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]     #= > 0.19
# # new_list = [i % 1 for i in source_list if i % 1 != 0]             #= > 0.19000000000000017
# print(f'{source_list} = > {max(new_list) - min(new_list)}')

#####################################################################

# import random
# N = int(input('Введите количество элементов массива: '))
# my_list = []

# for i in range(N):
#     my_list.append(round(random.uniform(0,100), 2))
# print(f'Исходный массив: {my_list}')

# count = 0

# for i in my_list:
#     while my_list[count] > 1:
#         my_list[count] +=  - 1
#     else:
#         count += 1
# print(f'Измененный массив: {my_list}')

# count = 0
# list_max = my_list[count]
# for i in my_list:
#     if i > list_max:
#         list_max = i
# print(f'Максимальное значение дробной части: {round(list_max, 2)}')

# count = 0
# list_min = my_list[count]
# for i in my_list:
#     if i < list_min:
#         list_min = i
# print(f'Минимальное значение дробной части: {round(list_min, 2)}')

# print(f'Разницу между максимальным и минимальным значением дробной части элементов равно: {round((list_max - list_min), 2)}')

###########################################################################

# import random
# N = int(input('Введите количество элементов массива: '))
# my_list = []

# for i in range(N):
#     my_list.append(round(random.uniform(0, 100), 2))
# print(f'Исходный массив: {my_list}')

# my_list = [round(val % 1, 2) for val in my_list]
# print(f'Измененный массив: {my_list}')
# rev_result = max(my_list) - min(my_list)
# print(round(rev_result, 2))

###########################################################################

# def inpun_int(msg= ""):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print('Ошибка повторите ввод')
#         else:
#             return result

# def input_float(msg=''):
#     while True:
#         try:
#             result = float(input(msg))
#         except ValueError:
#             print('Ошибка повторите ввод')
#         else:
#             return result

# def input_float_list():
#     count = inpun_int('Введите количество элементов списка: ')
#     result = list()
#     for i in range(count):
#         result.append(input_float(f'Введите вещественное число №{i + 1}: '))
#     return result

# def min_max_delta(input_list):
#     min = input_list[0]
#     max = input_list[0]
#     for i in input_list:
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#     return max - min

# def fraction_list(input_list):
#     fraction_list = list()
#     for i in input_list:
#         fraction_list.append(i - int(i))
#     return fraction_list

# print(min_max_delta(fraction_list(input_float_list())))



