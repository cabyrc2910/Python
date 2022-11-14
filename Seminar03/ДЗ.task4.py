# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
###################################################################

# n = int(input('Введите целое число: '))
# j = format(n, 'b')
# print(f'Цыфра {n} -> {j}')

##################################################################

# numb = int(input('Введите целое число: '))
# print(bin(numb))

# ###################################################################

# print((lambda x: str(x)+ "->" + str(bin(x)[2:]))(int(input("Enter a number: "))))

###################################################################
import os
os.system("cls")

n = (input('Введите число для преобразования: '))
while not n.isdigit():
   n = (input('Введите ещё раз: '))
n1 = int(n)
s = ''
while n1 != 0:
    s = str(n1 % 2) + s
    n1 //= 2
print(f'\nДесятичное число: {n} → двоичное число: {s}')


print(bin(int(n)))
# print(f'\n{bin(int(5))[2:]}')

####################################################################

# numb = int(input('Введите целое число: '))
# x = ''
# while numb != 0:
#     # x = str(numb % 2) + x 
#     x += str(numb % 2)  
#     numb = numb // 2
# print(f'Двоичное представление числа: {x}')

##################################################################

# import os
# from unittest import result
# os.system("cls")
# n = (input("Введите число для преобразования: "))
# while not n.isdigit():
#     n = (input("Введите еще раз: "))

# # n1 = int(n)  # ддя вывода стартового числа иначе обнулится
# # s = ""
# # while n1 != 0:
# #     s += str(n1 % 2)
# #     n1 //= 2
# # print(f'\nДесятичное число: {n} => двоичное число: {s}\n')

# # print(bin(int(n)))
# print(f'\nДвоичное число: {bin(int(n))[2:]}')

#####################################################################

# N = int(input('Введите число: '))
# my_list = []
# while N > 0:
#     ostatok = N % 2
#     N = N // 2
#     my_list.append(ostatok)
# my_list.reverse()
# print(my_list)

# binar = ''

# for i in my_list:
#     binar += str(i)
# print(binar)

###########################################################################

# def inpun_int(msg= ""):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print('Ошибка повторите ввод')
#         else:
#             return result

# def decimal_to_bin(number):
#     buffer = number
#     result = ''
#     while buffer > 0:
#         result = str(buffer % 2) + result
#         buffer //= 2
#     return result

# print(decimal_to_bin(inpun_int('Введите целое число: ')))

##############################################################################

