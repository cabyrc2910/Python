# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
##################################################

# my_text = '1-2*3*4*2+8/4+9-3+7'
# my_list = list(my_text)
# print(my_list)

# # не рекомендуемые функции
# # my_list = eval(my_text)
# exec(f'print({my_text})')
# i = 1

# while '*' in my_list or '/' in my_list:
#     if my_list[i] == '*':
#         my_list[i - 1] = int(my_list[i - 1]) * int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     elif my_list[i] == '/':
#         my_list[i - 1] = int(my_list[i - 1]) / int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     else:
#         i += 1

# i = 1

# while '+' in my_list or '-' in my_list:
#     if my_list[i] == '+':
#         my_list[i - 1] = int(my_list[i - 1]) + int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     elif my_list[i] == '-':
#         my_list[i - 1] = int(my_list[i - 1]) - int(my_list[i + 1])
#         del my_list[i + 1]
#         del my_list[i]
#     else:
#         i += 1

# # for i in range(len(my_list)):
# #     if my_list[i] == '*':
# #         my_list[i - 1] = str(int(my_list[i - 1]) * int(my_list[i + 1]))
# #         my_list[i + 1] = ' '
# #         my_list[i] = ''
# #     elif my_list[i] == '/':
# #         my_list[i - 1] = str(int(my_list[i - 1]) / int(my_list[i + 1]))
# #         my_list[i + 1] = ' '
# #         my_list[i] = ''

# print(my_list)

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# #         *Пример:*
# #         1+2*3 => 7;
# #         (1+2)*3 => 9;

#######################################
# Исправленный Итоговый вариант:

# def calc(my_list):
#     i = 1

#     while '*' in my_list or '/' in my_list:
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1

#     i = 1

#     while '+' in my_list or '-' in my_list:
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1
#     print('Выводим из функции результат:', my_list)
#     return my_list

####################################################

# my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
# my_list_out = list(my_text)
# print(my_list_out)

# while '(' in my_list_out:
#     bracket_left = my_list_out.index('(')
#     bracket_right = my_list_out.index(')')
#     my_list_out = my_list_out[:bracket_left] + calc(
#         my_list_out[bracket_left + 1: bracket_right]) + my_list_out[bracket_right + 1:]

# print(my_text + '=>' + str(calc(my_list_out)[0]))

############################################################
# ## Код Дмитрия
# my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
# my_list_out = list(my_text)
# # print(my_list_out)

# # my_list1 = eval(my_text)  # Не рекомендованная функция
# print(my_list_out)
# # exec(f'print({my_text})') # Не рекомендованная функция


# def calc(my_list):
#     i = 1

#     while '*' in my_list or '/' in my_list:
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1

#     i = 1

#     while '+' in my_list or '-' in my_list:
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else:
#             i += 1
#     return my_list


# while '(' in my_list_out:
#     bracket_left = my_list_out.index('(')
#     bracket_right = my_list_out.index(')')
#     my_list_out = my_list_out[:bracket_left] + calc(
#         my_list_out[bracket_left + 1: bracket_right]) + my_list_out[bracket_right + 1:]

# print(calc(my_list_out))
# # my_list = my_list[:до скобки] + функция(всё что в скобках) + my_list[от скобки +1:]

#############################################
# альиернатива
# def split_expression(expr):
#     buffer = ""
#     result = []
#     for digit in expr:
#         if digit.isdigit():
#             buffer += digit
#         else:
#             if buffer != "":
#               result.append(int(buffer))
#             result.append(digit)
#             buffer = ""
#     result.append(int(buffer))
#     return result


# def calculate(expr_list):
#     buffer_list = expr_list.copy()
#     index = 1
#     while "*" in buffer_list or "/" in buffer_list:
#         if buffer_list[index] == "*":
#             buffer_list[index] = buffer_list[index-1]*buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "/":
#             buffer_list[index] = buffer_list[index-1]/buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     index = 1
#     while "+" in buffer_list or "-" in buffer_list:
#         if buffer_list[index] == "+":
#             buffer_list[index] = buffer_list[index-1]+buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "-":
#             buffer_list[index] = buffer_list[index-1]-buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     return buffer_list[0]


# def calculate_with_brackets(expr_list):
#     buffer_list = expr_list.copy()
#     while "(" in buffer_list:
#       start = buffer_list.index("(")
#       end = buffer_list.index(")")
#       buffer_list[start] = calculate(buffer_list[start+1:end])
#       for i in range(end, start, -1):
#         buffer_list.pop(i)
#     return calculate(buffer_list)


# expr = "1-2*3*4*2+8/4+9-3+7"
# expr_bracket = "(1-2)*3*4*2+8/(4+9-3)+7"

# print(eval(expr))
# print(calculate( split_expression(expr)))


# print(eval(expr_bracket))
# print(calculate_with_brackets(split_expression(expr_bracket)))

####################################################################################################
# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(new_list)

# # V2
# new_lst = []
# [new_lst.append(i) for i in my_list if i not in new_lst]
# print(new_list)

# V3
# enum_number = list(map(int, input("input list:").split()))
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)


# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(my_list, '=>', new_list)

# Разбор
# enum_number = [1, 2, 3, 5, 1, 5, 3, 10]
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)

# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(filter_unique)
# print(list(filter_unique))
# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(tuple(filter_unique))
# for i in filter_unique:
#     print(i)

# ### уникальные
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(range(8,-4, -1)))
# for i in range(len(my_list) - 1,-1, -1):
#     if my_list.count(my_list[i]) != 1:
#         del my_list[i]

################################################################################
# Домашка урок 5
################################################################################

# def encoding(text):
#     code_text = ""
#     count = 0
#     repetitions = 1
#     while count < len(text):
#         try:
#             if text[count] == text[count+1]:
#                 repetitions += 1
#             elif repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#                 repetitions = 1
#         except IndexError:
#             if repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#         count += 1
#     return code_text
# # Function to decode given cipher


# def decoding(cipher):
#     decoded_text = ""
#     count = 0
#     repetitions = 0
#     while count < len(cipher):
#         if str(cipher[count]).isdigit():
#             repetitions = int(cipher[count])
#         elif repetitions > 0:
#             for x in range(repetitions):
#                 decoded_text += cipher[count]
#                 repetitions = 0
#         elif repetitions == 0:
#             decoded_text += cipher[count]
#         count += 1
#     return decoded_text


# # Text input
# text = input("Enter a text: ")
# # Decides encode or decode
# numbers_in_text = 0
# for num in text:
#     if num.isdigit():
#         numbers_in_text += 1
# # If any digits exists it mean coded text, decoding
# if numbers_in_text > 0:
#     print(f"Decoding: {decoding(text)}")
# # If no digits exists it mean pure text, encoding
# else:
#     print(f"Encoding: {encoding(text)}")
from math import ceil

x = int(2021 % 29)
y = 745 % 29
k = 1*29 - 28
print(x)
print(y)
print(k)