# Напишите программу, которая на вход ,будет принимать  чило  N  и выводить числа от -N до N
# Примеры:
# -5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

list(range(1, 6))  # [1,2,3,4,5]

list(range(0, 10, 2) )  # [0,2,4,6,8]

a= int(input())
print(list(range(-a, a+1)))

a= 5
for x in range(a):
    print (x, end=" ") 

for i in range(5):
    print(i)


N = int(input('Введите N: '))
for i in range(-N, N + 1):
    print(i, end=' ')


for i in range(0, 10, 2):
    print(i)        # [0,2,4,6,8]  в столбик

# printing a number
for i in range(0, 10, 2):
    print(i, end=' ')
print()                  # [0,2,4,6,8]