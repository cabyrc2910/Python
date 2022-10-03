# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#  6782 -> 23
#  0,56 -> 11


# # print('Вы ввели не число если сумма окажется = 0')
# number = input("Введите вещественное число: ") # создаём переменную для числа
# result = 0                                      # создаём счётчик переменную result приравниваем к "0"
# for i in number:                               # если переменная  i находится в числовом диапазоне, создаём условие
#     if i.isdigit():                             #  если в переменной i  все символы в строке являются цифрами, то
#         # result = result + int(i)                
#         result += int(i)                         # результат = предыдущий + i
# print(f"Сумма цифр числа {number} равна:', {result}")   #  вывод сообщения о результате



number = int(input('Введите вещественное число: '))
print(number)                                     
number_string = str(abs(number)) 
my_sum = 0
for i  in number_string:
    if i != ".": 
        my_sum += int(i)                                             
print(f"Сумма цифр числа {number} равна: {my_sum}")



# number = float(input('Введите вещественное число: '))
# z = str(number)
# print(z)
# list = []
# for i in range(len(z)):
#     list.append(z[i])   
# print('Заполненный массив из строк:', list) 
# for i in list:
#     if i == '.':
#         list.remove(i)
# print('Измененный массив:', list)
# sum = 0
# for i in list:
#     sum += int(i)
# print(f'Сумма цифр числа {number} равна:', sum)
