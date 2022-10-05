# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

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

# set_number = (input("Введите число: "))
# while not set_number.isdigit():
#     set_number = (input("Введите еще раз: "))
# set_number = int(set_number)
# list = [0]
# for i in range(1, set_number + 1):
#     list.append(fibonacci(i))
#     list.insert(0, negative_fibonacci(i))
# print(list)



fib1 = 1
fib2 = -1
fib_negative = []
fib_negative.append(fib1)
fib_negative.append(fib2)

n = int(input('Введите n: '))

for i in range(-n, -2):
    fib1, fib2 = fib2, fib1 - fib2
    fib_negative.append(fib2)

fib_negative.reverse()
fib_negative.append(0)

fib1 = fib2 = 1
fib_negative.append(fib1)
fib_negative.append(fib2)

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_negative.append(fib2)
print(fib_negative)


