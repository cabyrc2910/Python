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


my_text = '1-2*3*4*2+8/4+9-3+7'
my_list = list(my_text)
print(my_list)

# не рекомендуемые функции
# my_list = eval(my_text)
exec(f'print({my_text})')
i = 1

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

# for i in range(len(my_list)):
#     if my_list[i] == '*':
#         my_list[i - 1] = str(int(my_list[i - 1]) * int(my_list[i + 1]))
#         my_list[i + 1] = ' '
#         my_list[i] = ''
#     elif my_list[i] == '/':
#         my_list[i - 1] = str(int(my_list[i - 1]) / int(my_list[i + 1]))
#         my_list[i + 1] = ' '
#         my_list[i] = ''

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
## Код Дмитрия
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
# альтернатива

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














