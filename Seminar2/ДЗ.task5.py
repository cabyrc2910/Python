# Реализуйте алгоритм перемешивания списка.

# import random
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Исходный список: {list}')
# random.shuffle(list)
# print(f'Перемешанный список: {list}')


# import random
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('Исходный список: ', lst)
# mix_lst = random.sample(lst, len(lst))
# print('Перемешанный список:', mix_lst)


# temp = 0                               #  создаётся переменная temp
# size = int(input('Enter a list size:'))  #  ввод пользователя   "5"
# numbers = list(range(size))                #  создаётся список с диапозоном от 0 до 5
# print(numbers, end = ' ')                
# temp = 0
# for i in numbers:                     #  распечатываем полученный список
#     temp = numbers[i]                   #  перебираем список
#     numbers.pop(i)                        # берём "numbers функции pop" 
#     numbers.append(temp)       # убираем "0" элемент, перебрасываем в конец в (for i in numbers:)
# print(numbers, end= ' ')              

# алгоритм перетасовки Фишера–Йейтса
# import random
# lst = [1,2,3,4,5]
# print("Исходный список: ", lst)



# for i in range(len(lst) -1, 0, -1):
#     j = random.randint (0, i + 1)       #  берём случайный индекс от 0 до i
#     lst[i],lst[j] = lst[j],lst[i]          #  меняем arr[i] c элементом случайного индекса
# print("перемешиваем список: ", lst)



my_list = [2,3,56,45,34,2,6,78,3,1,9]
my_list = list(set(my_list))               #  set - множество - "контейнер", содержащий не повторяющиеся элементы в случайном порядке
print("перемешиваем список: ", my_list)