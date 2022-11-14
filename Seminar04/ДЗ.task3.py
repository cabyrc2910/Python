#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Например: [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] -> [6, 2, 3, 0, 9]

##########################################################################

my_list = [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
new_list = []
for i in my_list:
    if my_list.count(i) == 1:
        new_list.append(i)
print(new_list)       # [6, 2, 3, 0, 9]

###########################################################################

# new_lst = []
# [new_lst.append(i) for i in my_list if i not in new_lst]
# print(new_list)

############################################################################

# enum_number = list(map(int, input("input list:").split()))
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)

#############################################################################

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(my_list, '=>', new_list)

###############################################################################

# my_list = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"\nИсходный список: {my_list}")
# new_list = []
# [new_list.append(i) for i in my_list if i not in new_list]
# print(f"\nСписок из неповторяющихся элементов: {new_list}")

###############################################################################

# # Разбор
# enum_number = [1, 2, 3, 5, 1, 5, 3, 10]
# enum_unique = list(
#     filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)

# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(filter_unique)
# print(list(filter_unique))
# filter_unique = filter(lambda item: enum_number.count(item) == 1, enum_number)
# print(tuple(filter_unique))
# for i in filter_unique:
#     print(i)

##############################################################################

# ### уникальные
# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(range(8,-4, -1)))
# for i in range(len(my_list) - 1,-1, -1):
#     if my_list.count(my_list[i]) != 1:
#         del my_list[i]

##############################################################################

# from random import randint
# def isfloat(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#        return False
# lengthList = input('Введите целое число:')
# while isfloat(lengthList) ==False:
#     lengthList = input('Введите целое число:')
# lengthList = int(lengthList)
# myList = []
# for ilem in range(lengthList):
#     myList.append(randint(0, lengthList))
# print(myList)
# myNewList = []
# for elem in range(len(myList)):
#     if myList.count(elem) ==1:
#         myNewList.append(elem)
# print(myNewList)     #  Введите целое число:6    [3, 4, 4, 5, 5, 2]  [2, 3]



