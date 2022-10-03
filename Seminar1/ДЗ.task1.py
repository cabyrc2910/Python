# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#  6 -> да
#  7 -> да
#  1 -> нет

DAY_NUM = int(input('Введите номер дня недели от 1 до 7: '))
if DAY_NUM == 6 or DAY_NUM == 7:
    print('да')
else:
    print('нет')



import os
os.system('cls')  # использование функции очистки терминала, подключение библиотеки "os"

day = int(input('Введите номер дня недели = '))
if 0<day<6:
    print(day,'нет',sep='->')
elif 0>=day or day>7:
    print('Такого дня недели нет')
else:
    print(day,'да', sep='->')



day = input('Введите номер дня недели = ')
while day not in ('1','2','3','4','5','6','7')  # range(1,8): - имеет 3 аргумента (start, stop, step), isdigit  - все символы в строке цыфры
    print('Такого дня недели нет')
    day = input('Введите номер дня недели')
day = int(day)

if 0<day<6:
    print(day,'нет',sep='->')
elif 0>=day or day>7:



if 5 > int (input('Введите номер дня недели: ')) < 8:  # если введённая переменная брольше 5 и при этом меньше 8, то
    print('да')  # да, является
else: # иначе
    print('нет') #  нет не является


def InputNumbers(inputText):
    check_input = False
    while not check_input:
        try:
            number = int(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print('Вы вводите не цыфр, введите корректные данные')
    return number


def CheckDaysofWeek(day):
    if day < 1 or day > 7:
        print('Введите число соответствующее дню недели')
    elif day == 6 or day == 7:
        print('Выходной! ')
    else:
        print('будний день...')
day = InputNumbers ('Введите цыфру, обозначающую день недели:')
CheckDaysofWeek(day)