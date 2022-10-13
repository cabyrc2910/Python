
my_text = '1-2*3*4*2+8/4+9-3+7'
my_list = list(my_text)
print(my_list)

# не рекомендуемые функции
# my_list = eval(my_text)
exec(f'print({my_text})')
i = 1

while '*' in my_list or '/' in my_list:
    if my_list[i] == '*':
        my_list[i - 1] = int(my_list[i - 1]) * int(my_list[i + 1])
        del my_list[i + 1]
        del my_list[i]
    elif my_list[i] == '/':
        my_list[i - 1] = int(my_list[i - 1]) / int(my_list[i + 1])
        del my_list[i + 1]
        del my_list[i]
    else:
        i += 1

i = 1

while '+' in my_list or '-' in my_list:
    if my_list[i] == '+':
        my_list[i - 1] = int(my_list[i - 1]) + int(my_list[i + 1])
        del my_list[i + 1]
        del my_list[i]
    elif my_list[i] == '-':
        my_list[i - 1] = int(my_list[i - 1]) - int(my_list[i + 1])
        del my_list[i + 1]
        del my_list[i]
    else:
        i += 1

# for i in range(len(my_list)):
#     if my_list[i] == '*':
#         my_list[i - 1] = str(int(my_list[i - 1]) * int(my_list[i + 1]))
#         my_list[i + 1] = ' '
#         my_list[i] = ''
#     elif my_list[i] == '/':
#         my_list[i - 1] = str(int(my_list[i - 1]) / int(my_list[i + 1]))
#         my_list[i + 1] = ' '
#         my_list[i] = ''

print(my_list)

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
my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
my_list_out = list(my_text)
# print(my_list_out)

# my_list1 = eval(my_text)  # Не рекомендованная функция
print(my_list_out)
# exec(f'print({my_text})') # Не рекомендованная функция


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


################################################################################
# Домашка урок 5
################################################################################




# from math import ceil

# x = int(2021 % 29)
# y = 745 % 29
# k = 1*29 - 28
# print(x)
# print(y)
# print(k)