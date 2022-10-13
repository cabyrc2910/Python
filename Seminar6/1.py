##############################################################################
# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции (+,-,/,*), приоритет операций стандартный.
#  Пример:   2+2 => 4;
#            1+2*3 => 7;
#            1-2*3 => -5;
#  Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример: 1+2*3 => 7
#         (1+2)*3 => 9
##############################################################################

# def my_action(op, digit_1, digit_2):
#     if op == '+':
#         return digit_1 + digit_2       # my_string = '1+2*3+4/2'
#     elif op == '-':                    # id_digit = 0 1 2 3 4
#         return digit_1 - digit_2       # id_simbol = 0 1 2 3
#     elif op == '/':
#         return digit_1 / digit_2       # my_string = '1+6+2'
#     elif op == '*':                    # id_digit = 0 1 2
#         return digit_1 * digit_2       # id_simbol = 0 1

# my_string = '1+2+3*5-6/3+7-9*0'
# my_list_simbols = [i for i in my_string if not i.isdigit()]
# my_list_digits = [int(i)for i in my_string if i.isdigit()]

# while '*' in my_list_simbols or '/' in my_list_simbols:
#     for i, e in enumerate(my_list_simbols):
#         if i in('*','/'):
#             my_list_digits[i] = my_action(
#                 e, my_list_digits[i], my_list_digits[i+1])
#             del my_list_digits[i+1]
#             del my_list_simbols[i]
# while len(my_list_simbols) > 0:
#     for i, e in enumerate(my_list_simbols):
#         my_list_digits[i] = my_action(
#             e, my_list_digits[i], my_list_digits[i+1])
#         del my_list_digits[i+1]
#         del my_list_simbols[i]

# # print(my_list_simbols)
# print(my_list_digits)

#  Функция (pop)-  удаляет из списка и возвращает вместо себя этот элемент

##########################################################################
# 1.1 Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример: 1+2*3 => 7
#         (1+2)*3 => 9          при помощи рекурсии
##########################################################################

# def my_action(op, digit_1, digit_2):
#     if op == '+':
#         return digit_1 + digit_2       # 
#     elif op == '-':                    # 
#         return digit_1 - digit_2       # 
#     elif op == '/':
#         return digit_1 / digit_2       # 
#     elif op == '*':                    # 
#         return digit_1 * digit_2       # 

# def brackets(my_string):
#     my_list_simbols = [i for i in my_string if not i.isdigit()]
#     my_list_digits = [int(i)for i in my_string if i.isdigit()]
#     while '*' in my_list_simbols or '/' in my_list_simbols:
#         for i, e in enumerate(my_list_simbols):
#             if i in('*','/'):
#                 my_list_digits[i] = my_action(
#                     e, my_list_digits[i], my_list_digits[i+1])
#                 del my_list_digits[i+1]
#                 del my_list_simbols[i]
#     while len(my_list_simbols) > 0:
#         for i, e in enumerate(my_list_simbols):
#             my_list_digits[i] = my_action(
#                 e, my_list_digits[i], my_list_digits[i+1])
#             del my_list_digits[i+1]
#             del my_list_simbols[i]
#     return str(my_list_digits[0])


# my_string_out = '(1+2)+(3*5-6/3+7-9*0)*3*4'

# while '(' in my_string_out:
#     i_bracket_l = my_string_out.index(')')
#     i_bracket_r = my_string_out.index(')')
#     my_string_out = my_string_out[:i_bracket_l] +\
#          brackets(my_string_out[i_bracket_l+1:i_bracket_r]) + \
#             my_string_out[i_bracket_r:]
#     print(my_string_out)

# # print(my_list_simbols)
# print(my_string_out)

################################

# a = 0
# ex = 'a = 1+2*' + input('ssa')
# print(ex)   # ssa5
# exec(ex)    # a = 1+2*5
# print(a)    # 11

#############################

# a = input()    # 1+2*3
# exec(f'a = {a}')
# print(a)       # 7

##########################################################################
















