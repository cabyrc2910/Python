# **Задача:** Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# список и строка
# my_dict = {3: 'Иванов', 1: 'Васльев', 4: 'Петров'}


# for elem in sorted(my_dict):
#     print(elem)
#     print(elem, my_dict[elem])

# for key, value in sorted(my_dict.items()):
#     print(key, value)

# print(my_dict)
# print(sorted(my_dict))
# print(my_dict.items())
# print(type(my_dict.items()))
# print(sorted(my_dict.items()))
# print(my_dict.keys())
# print(sorted(my_dict.keys()))
# print(my_dict.values())
# print(sorted(my_dict.values()))

# my_list = [(1, 'a', True), (2, 'b', False), (3, 'x', True)]
# for first, second, third in my_list:
#     print(first)
#     print(second)
#     print(third)
#     print()
#     print('Следующй цилк')

my_dict = {'три': 'Иванов', 'один': 'Васильев',
           'четыре': 'Петров', 'шесть': 'Иванов'}
print(my_dict)

my_dict['два'] = my_dict.pop('четыре')
print(my_dict)

my_dict['три'] = my_dict['три'] + ' ' + my_dict.pop('один')
print(my_dict)

my_dict[0] = 'Привет)'
print(my_dict)

print(my_dict[1])