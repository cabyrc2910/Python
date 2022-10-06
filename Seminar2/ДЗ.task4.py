# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

#######################################################################

size = int(input("Введите  число N: "))
numbers_list = list(range(-size, size+1))      # задаём список  [-N, N]
path = 'Seminar2/ДЗ.task4.txt'                     # задаём путь к файлу
data = open(path, 'r')
sum = 1
for position in data:
    sum *= numbers_list[int(position)]        #  sum = numbers_list[int(position)]*sum
data.close()
print(numbers_list)
print(sum)

######################################################################

# import os
# import random
# os.system("cls")

# def write_file(number):
#     with open('Seminar2/ДЗ.task4.txt', 'w') as data:
#         for i in range(number):
#             data.write(f"{random.randrange(0, 2*number)}\n")


# def read_file():
#     with open('Seminar2/ДЗ.task4.txt', 'r') as data:
#         indexs = list(map(int, data.readlines()))
#     return indexs

#######################################################################

# n = int(input("Введите число N: "))
# lst_number = [i for i in range(-n, n+1)]
# write_file(n)
# lst_index = read_file()
# prod = 1
# for i in range(len(lst_index)):
#     prod *= lst_number[lst_index[i]]
# print(f'\nРезультат:')
# print(f'список элементов -> {lst_number}')
# print(f'позиции из файла -> {lst_index}')
# print(f'произведение элементов -> {prod}\n')

