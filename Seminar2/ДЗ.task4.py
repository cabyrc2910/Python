# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# N = int(input('Введите N: '))
# list = []
# for i in range(N):
#     list.append(random.randint(-N, N))
# print(list)

# pro = 1

# data = open('C:\Users\Иван\Desktop\GeekBrains\Python\2sem.ДЗ.task4\file.txt', 'r')
# for i in data:
#     pro = pro * list[int(i)]
# print(f'Произведение элементов {list[1]} и {list[3]} равно: {pro}')
# data.close()



N = int(input('Введите  число N: '))
numbers_list = list(range(-N, N+1))
path = 'file.txt'
data = open(path,'r')
sum = 1
for i in data:
    sum *= numbers_list[int(i)]
data.close()
print(numbers_list)
print(sum)
