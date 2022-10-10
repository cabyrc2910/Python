#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

####################################################################

from random import randint
import os
os.system("cls")

k = (input("Введите натуральную степень k = "))
while not k.isdigit():
    k = (input("Введите еще раз: "))
k = int(k)
result = ''
for i in range(k, 0, -1):
    a = '*x^' + str(i)
    result += (str(randint(0, 100)) + a + ' + ')
polinomial = result + str(randint(0, 100)) + '= 0'
data = open('Seminar4\ДЗ.task4.txt', 'w')
data.writelines(polinomial)
data.close()
with open('Seminar4\ДЗ.task4.txt', 'r') as data:  # попробуем with
    print(
        f'Многочлен степени "{k}" = {data.readlines()}')

################################################################
