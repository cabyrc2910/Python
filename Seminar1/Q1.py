# Напишите программу, которая принимает на вход 2 числа и проверяет, является ли одно число квадратом другого
# Примеры:
# 5, 25 -> да
# 4, 26 -> да
# 25, 5 ->  да
# 8, 9 -> нет

a = int(input())
b = int(input())
if a**a == b:
    print('да')
else:
    a != b
    print('нет')