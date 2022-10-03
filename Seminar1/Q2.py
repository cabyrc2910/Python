# Напишите программу, которая на вход принимает  5 чисел и находит максимальное из них
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# mx = max(list([a,b,c,d,e]))
# print(mx)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print (max(list([a, b, c, d, e])))


# number_list = list (map(int, input().split())) #  map склеивает int и  input и через list возвращает
# print(max(number_list) )


# a = [10, 2, 3, 4, 5]
# max = a[0]
# for i in a:
#     if i > max:
#         max = i
# print(max)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
e = int(input('Введите пятое число: '))
numbers = [a,b,c,d,e]
max = a
for i in numbers:
    if i > max:
        max = i
print('Максимальное число: ', max)