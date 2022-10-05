# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


# my_list = ["123", "234", '12333', "567", '123']
# namber = '123'
# for i in my_list:
#     if namber in i:
#         print(i)
#         print(my_list.index(i))        # 123 0 12333 2 123 0


# my_list = ["123","234", "12333", "567", "123"]
# number = "123"
# nul = 0
# for elem in my_list:
#     if number in elem:
#         print(elem)
#         print(my_list.index(elem, nul))
#         nul = my_list.index(elem, nul) + 1     # 123 0 12333 2 123 4


my_list = ["123", "234", "12333", "567", "123"]
number = "123"
for i, elem in enumerate(my_list):      # enumerate переберает и элементы и индексы как range
    if number in elem:
        print(elem)
        print(i)                        # 123 0 12333 2 123 4
