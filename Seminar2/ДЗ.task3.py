# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:                                                        (i + 1 /n)**n
# Для n = 6: {2, 4, 1, 1, 1, 1}: 10    


# N = int(input('Введите N: '))
# list = []
# for i in range(1, N + 1):
#     list.append(round(1 + 1/i)**i)
# print(list)
# sum = 0
# for i in list:
#     sum += i
# print(f'Сумма чисел последовательности равна:', sum)   # [2, 4, 1, 1, 1, 1] 10
 


# is_Ok = True
# while is_Ok:
#     try:
#         n = input('Введите число N: ')
#         n = float(n)
#         n = int(n)
#         is_Ok = False
#     except ValueError:
#         print('Вводить надо число')
# lst = []
# for i in range(1,n+1):
#     s = (1 + 1/i)**i
#     s = round(s)
#     lst.append(s)
# print(f'Полученная сумма последовательности {lst} =', sum(lst))  # [2, 2, 2, 2, 2, 3] = 13



# def input_int(msg):
#     while True:                                            # запускаем бесконечный цикл
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print('Ошибка, повторите ввод: ')
#         else:
#             return result
# def generate_list(n):                                      # генерация списка
#     result = []                                            # задаём пустой список
#     for i in range(1, n + 1):                              # задаём проход по набору элементов заканчивая  n + 1
#         result.append(round(1 + 1/i)**i)                   # на каждом проходе добавляем округлённое число
#     return result                                          # после прохода списка возврвщаем результат

# n = input_int('Введите целое число:')                      # вводим число
# number_list = generate_list(n)                             # получаем сгенерированный список

# print(f'Для n = {n}:{number_list} → {sum(number_list)}')  # возвращаем список и сумму списка  n = 6:[2, 4, 1, 1, 1, 1] → 10


def is_int(number):
    return number.isdigit()
number = None
while not is_int(str(number)):
    number = input('input number:')
number = int(number)

result = dict()
for i in range(1, number+1):
    result[i] = round((1 + 1 /i) **i)
my_sum = 0
for i in result:
    my_sum += result[i]
print(result, '→', my_sum)    #   {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3} → 13