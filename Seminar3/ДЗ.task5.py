#######################################################################################################################
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# F−1 = 1,   F−2 = -1,    Fn = F(n+2)−F(n+1).         F−n = (−1)n+1Fn.
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
###########################################################################################################################

# fib = lambda n: fib(n-1) + fib(n-2) if n >2 else 1
# fib_list = [fib(x) for x in range(int(input("Enter a number:"))) if x > 0]
# print(list([i for sublist in[list(z)for z in zip(reversed([-x for n, x in enumerate(fib_list)if n%2==1]),\
#  reversed([x for n, x in enumerate(fib_list)if n%2==0]))] for i in sublist]) + [0] + fib_list)

################################################################

collection = [2, 3, 4, 9, 1, 3]
length = len(collection)
print(list(map(lambda i: collection[i] * collection[length - i - 1], range(length // 2 + length % 2))))
 
################################################################

# set_number = (input("Введите число: "))
# while not set_number.isdigit():
#     set_number = (input("Введите еще раз: "))
# set_number = int(set_number)
# list = [0]
# for i in range(1, set_number + 1):
#     list.append(fibonacci(i))
#     list.insert(0, negative_fibonacci(i))
# print(list)

###############################################################

# import os
# os.system("cls")

# def fibonacci(n):
#     first, second = 0, 1
#     fibonacci_num = 0
#     for i in range(n):
#         fibonacci_num = first + second
#         second = first
#         first = fibonacci_num
#     return fibonacci_num

# def negative_fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

###############################################################

# fib1 = 1
# fib2 = -1
# fib_negative = []
# fib_negative.append(fib1)
# fib_negative.append(fib2)

# n = int(input('Введите n: '))

# for i in range(-n, -2):
#     fib1, fib2 = fib2, fib1 - fib2
#     fib_negative.append(fib2)

# fib_negative.reverse()
# fib_negative.append(0)

# fib1 = fib2 = 1
# fib_negative.append(fib1)
# fib_negative.append(fib2)

# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     fib_negative.append(fib2)
# print(fib_negative)

#####################################################################

# def inpun_int(msg= ""):
#     while True:
#         try:
#             result = int(input(msg))        # вводим число, пытаемся привести к целому
#         except ValueError:                   #  ошибка пользовательского ввода
#             print('Ошибка повторите ввод')  #  если не приводится выходим обратно в цикл , пытаемся ввести снова
#         else:
#             return result                    #  если приводится то выходим с функцией

# def positive_fibonacci(n):
#     if n > 0:
#         return[]
#     if n == 0:
#         return[0]
#     if n == 1:
#         return[0, 1]
#     result = list()
#     result.append(0)
#     result.append(1)
#     for i in range(2,n+1):
#         result.append(result[i - 1] + result[i - 2])
#     return result

# def revers_list(input_list):
#     result = list()
#     length = len(input_list)
#     for i in range(length):
#         result.append(input_list[length - i -1])
#     return result

# def negative_fibonacci(n):
#     if n <= 0:
#         return[]
#     if n == 1:
#         return[1]
#     if n == 2:
#         return[-1, 1]
#     result = list()
#     result.append(0)
#     result.append(1)
#     result.append(-1)
#     for i in range(3,n+1):
#         result.append(result[i - 2] + result[i - 1])
#     result.pop(0)
#     return revers_list(result)

# def full_fibonacci(n):
#     return negative_fibonacci(n) + positive_fibonacci(n)

# print(full_fibonacci(inpun_int('Введите целое число: ')))


