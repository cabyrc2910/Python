# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Например: 54 -> [2, 3, 3, 3]

###########################################################

# N = 54
# my_list = []
# factor = 2
# while N > 1:
#     if N % factor == 0:
#         my_list.append(factor)
#         N = N / factor
#     else:
#         factor += 1
# print(my_list)

#############################################################

# n = (input("Введите число : "))
# while not n.isdigit():
#     n = (input("Введите еще раз: "))
# n = int(n)
# num = n
# i = 2  # первое простое число
# new_list = []
# while i <= n:
#     if n % i == 0:
#         new_list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"\nПростые множители числа {num} приведены в списке: {new_list}")

########################################################################

n = int(input('Введите число: '))
lst = []
for i in range(2, n**0,5):
    if n % i == 0:
        count = 1
        for j in range(2, (i/2 + 1)):
            if (i % j == 0):
                count = 0
                break
        if (count == 1):
            lst.append(i)
print(lst)
