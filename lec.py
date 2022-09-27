# Типы данных и переменная
# int, float, boolean, str, list, None
# print('hello world')
from cProfile import run
from cgitb import text
from imp import new_module


value = None
a = 123
b = 1.23
print(type(a))
print(type(b))

value = 12334
# print(type(value))
s = 'hello "world'  # кавычки
# s = 'hello \nworld'  # переход на новую строку
a = 123
b = 1.23
# print(s) # вывод строки
# print(a, b, s) # вывод нескольких переменных
# print(a, '-',b, '-', s) # вставка дополнительных строк
# print('{1} - {2} - {0}'.format(a, b, s)) # форматированный вывод
# print(f'{a} - {b} - {s}') # форматированный вывод
# f= True # логическая переменная
# print(f)

list = [] # обьявление массива
list = ['1','2','3','hello']
list = ['1','2','3','hello',1,2,3,4.5,True]
list = ['1','2','3']
col = ['hello',1,2,3,4.5,True]
print(list)
print(col)

# Ввод и вывод данных  input() и print()  
print('Введите a'); # ввод, записываем переменную
# a = input()  # присваиваем input,  работа со строками
# a = int(input())  #   работа с числовым форматом
a = float(input())  #  работа с вещественными значениями
print('Введите b');
# b = input()       #   работа со строками
# b = int(input())  #   работа с числовым форматом
b = float(input())  #  работа с вещественными значениями
# print(a,b) # распечатываем
# print(a, '+',b, '=', a+b) # сумма двух чисел 1020
# print('{} {}'.format(a,b))
print(f'{a} {b}')

# Арифметические операции
# Приоритет операций           +,-,*,/,%(процент от деления),//(деление в целых числах),**(возведение в степень)
# Скобки меняют приоритет ()   **,  ,  ,*,/,//,%,+,-
# a = 2
# b = 8
# # c=a+b
# c=round(a*b,5) # округление до 5 знаков
# print(c)
# Сокращённые операции присваивания
a = 3
a *= 5
print(a)

# Логические операции   >,>=,<,<=<==<!=    not,and,or     is,is not,in,not in
a = 1 < 4 and 5 > 3
a == 1 == 2 # операция сравнения
a == 1 != 2 # операция неравенства
print(a)

a = 'qwe' # операция сравнения
b = 'qwe' 
print(a == b) # Сравнение (a) и (b) == истина (True)

a = [1,2] # операция сравнения списков
b = [1,2]  
print(a == b) # получаем истина (True) - списки сравниваются поэлементно

a = 1 < 3 < 5 # операция сравнения тройного неравенства
print(a) 

func = 1
T = 4
x = 2
print(func<T>(x)) # операция сравнения тройного неравенства

F = 1 > 2 or 4 < 6  # логическая операция
print(f)

f = [1,2,3,4]
print(f)
# print(2 in f) # получаем истину
print(not 2 in f) # получаем отрицание

# is_odd = f(0) % 2 == 0 #  по умолчанию 0 = Folse, 1 = True
is_odd = not f(0) % 2
print (is_odd)

# Управляющие конструкции: if, if-else  операторы ветвления
a = int(input('a = '))   #  нахождение максимума из 2 чисел
b = int (input('b = '))  # считываем 2 число
if a > b:          #  делаем проверку 
    print(a)
else:
    print(b)    


username = input('Введите Имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина!')
elif username== 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)

# Управляющие конструкции: while  выполнение блока операторов какое-то колдичество раз
original = 23
inverted = 0  # собираем число инвертируемое
while original != 0:
    iverted = inverted * 10 + (original % 10) # компануем
    original //= 10                           # перевёрнутое число
print(inverted)


original = 23
inverted = 0
while original != 0:
    iverted = inverted * 10 + (original % 10)
    original //= 10 
print(original)
else:                  # выполняется в том случае когда основное тело цикла перестаёт работать
    print('Пожалуй')
    print('хватит')                          
print(inverted)

# Управляющие конструкции: for  выполнение в том случае когда мы знаем что хотим
for i in 1,2,3,4,5:
    print(i**2)  # квадрат этих чисел, выводится  32


list = [1,2,3,4,10,5] # список 
for i in list:
    print(i)  # выводится от 1,2,3,4,10,5


r = range(10)  # 
for i in r:
    print(i)    # выводится от 0,1,2,3,4,5,6,7,8,9


for i in range(5):
    print(i)     # выводится от 0,1,2,3,4

    for i in range(1, 5):
    print(i)     # выводится от 1,2,3,4 

    for i in range(1, 10, 2):
    print(i)     # выводится  1,3,5,7,9

      for i in 'qwerty':
    print(i)     # выводится  q,w,e,r,t,y

# Работа со строками
text = 'съешь ещё этих мягких французких булок'
text.
print(len(text))                  # 39
print('ещё' in text)              # True
print(text.insdigit())            # False
print(text.islower())             #True
print(text.replace('ещё','ЕЩЁ'))  # 
for c in text:
    print(c)


# Срезы - представление строки как массива символов - обращение к элементу строки по его индексу
text = 'съешь ещё этих мягких французких булок'
print(text[0])                # с
print(text[1])                # Ъ
# print(text[len(text)])        #  Index error
print(text[len(text)-1])      # к
print(text[-5])             # б
print(text[:])                # print (text)  по умолчанию (text[0:len(text)-1]) 
print(text[0:2])            # съ
print(text[len(text)-2:])     # ок
print(text[2:9])            # ешь ещё
print(text[6:-18])            # ещё этих мягких
print(text[0:len(text):6])    # сеикакл
print(text[::6])              # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...


# Списки: пронумерованная изменякемая коллекция 
## list = list

numbers = [1,2,3,4,5]
print(numbers)            # [1,2,3,4,5]
ran = range(1,6)
print(type(run))
numbers = list(run)      # приведение типа run к типу list
print(type(run))         
print(numbers)            # [1,2,3,4,5]
numbers[0] = 10
print(f'{len(numbers)}len')
print(numbers)            # [1,2,3,4,5]
for i in numbers:
    i  *= 2
    print(i)              # [20,4,6,8,10}
print(numbers)            # [10,2,3,4,5]



colors = ['red', 'green','blue']

for e in colors:
    print(e)                 # red green blue

for e in colors:
    print(e*2)               # redred greengreen blueblue

colors.append('gray')        # добавить в конец
print(colors == ['red', 'greeen', 'blue', 'gray'])   #  True
colors.remove('red')         #  del colors[0] # удалить элемент 


# функции - фрагмент программы используемый многократно

def function_name(x):
  #  bodi line 1
  # .....
  #  bodi line n
  #  optional return

  def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1  
print(f(arg))
print(type(f(arg)))
