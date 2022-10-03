# Напишите программу, которая на вход ,будет принимать  дробь и показывать первую цифру дробной части чмсла
# Примеры:
# -6,78 -> 7, -5 -> нет, 0,34 -> 3, 

a = float(input())
b = int( (a*10)%10 )
print (b)   

a = float(6,78)
a


int((a*10)%10)


a = float(input())
b = int( (a%1)
print (b)


round(66,7)   # 67


a = str(input('Введите дробное число: '))
count = 0
not_s = 0
for i in a:
    count += 1
    if i == ".":
        not_s = 1
        print(a[count])
if not_s == 0:
    print("Нет")