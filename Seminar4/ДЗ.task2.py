# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Например: 54 -> [2, 3, 3, 3]

N = 650
my_list = []
factor = 2
while N > 1:
    if N % factor == 0:
        my_list.append(factor)
        N = N / factor
    else:
        factor += 1
print(my_list)