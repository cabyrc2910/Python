# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

##########################################################################

# from random import random

# list = [2, 3, 5, 9, 3]
# my_summ = 0
# for i in range(len(list)):
#     if i % 2:
#         my_summ += list[i]
# print(f"Сумма равна: {my_summ}")

############################################################################

# my_list = [2, 3, 5, 9, 3]
# suma = 0
# count = 0
# for i in my_list:
#     if count % 2 == 0:
#         count += 1
#     else:
#         suma += i
#         count += 1
# print(suma)

##############################################################################

# my_list = [2, 3, 5, 9, 3]
# num_sum = 0
# for item in range(1, len(my_list), 2):
#     num_sum += my_list[item]
# print(num_sum)

###############################################################################

# my_list = [2, 3, 5, 9, 3]
# print(f'Sum => {sum(my_list[1::2])}')

##############################################################################

import random
my_list = [random.randint(0,9)for x in range(random.randint(5,10))]
odd_list = [x for n, x in enumerate(my_list) if n %2 != 0]
print(f'{my_list} => odd indexes has values {" и ".join(map(str, odd_list))}, sum is{sum(odd_list)}')

###############################################################################
# import random
# num = int(input('Введите число: '))
# num_list =[]
# for i in range(num):
#     num_list.append(random.randint(1, 10))
# print(num_list)  
# print(sum(num_list[::2]))   #   срез, складываем элементы cписка через один начиная с первого

#################################################################################

# def inpun_int(msg= ""):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print('Ошибка повторите ввод')
#         else:
#             return result

# def input_int_list():
#     count = inpun_int('Введите количество элементов списка ')
#     result = []
#     for i in range(count):
#         result.append(inpun_int(f'Введите целое число № {i+1}: '))
#     return result

# def sum_of_odd(number_list):
#     result = 0
#     for i in range(len(number_list)):   # перебор по нумерам индексов от 0 до длины -1
#         if i % 2 == 1:                  # проверяемна нечётность по каждому из индексов остаток от деления на 2 == 1
#             result += number_list[i]
#     return result

# print(sum_of_odd(input_int_list()))
