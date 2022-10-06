# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
###############################################################################

# import os
# os.system("cls")
# # исходный список
# source_list = [2, 3, 4, 5, 6]

# # вариант 1
# counting_pairs1 = 0
# if len(source_list) % 2 != 0:
#     counting_pairs1 = len(source_list)//2 + 1
# else:
#     counting_pairs1 = len(source_list)//2
# new_list1 = []
# for i in range(counting_pairs1):
#     new_list1.append(source_list[i]*source_list[-i-1])
# print(f'Вариант 1: {source_list} = > {new_list1}')

# # вариант 2, можно сократить

# counting_pairs2 = len(source_list) // 2 + \
#     1 if len(source_list) % 2 != 0 else len(source_list)//2
# new_list2 = [source_list[i] *
#              source_list[len(source_list)-i-1] for i in range(counting_pairs2)]
# print(f'\nВариант 2: {source_list} = > {new_list2}')

####################################################################################

# import random
# N = int(input('Введите количество элементов массива: '))
# my_list = []
# for i in range(N):
#     my_list.append(random.randint(0, 9))
# print(my_list)

# new_list = []
# x = 0
# y = N - 1

# if N % 2 == 0:
#     for i in my_list:
#         if x >= y:
#             break
#         else:
#             new_list.append(i * my_list[y])
#             y -= 1
#             x += 1
# if N % 2 == 1:
#     for i in my_list:
#         if x >= y:
#             new_list.append(i)
#             break
#         else:
#             new_list.append(i * my_list[y])
#             y -= 1
#             x += 1
# print(new_list)

#########################################################################

def inpun_int(msg= ""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print('Ошибка повторите ввод')
        else:
            return result

def input_int_list():
    count = inpun_int('Введите количество элементов списка ')
    result = []
    for i in range(count):
        result.append(inpun_int(f'Введите целое число № {i+1}: '))
    return result

def pair_production(input_list):
    length = len(input_list)
    target_length = length//2                # целая часть от деления на 2 (количество пар)
    result = []
    for i in  range(target_length):
        result.append(input_list[i] * input_list[- i - 1])
    if length % 2 != 0:
        result.append(input_list[target_length]** 2)
    return result

print(pair_production(input_int_list()))