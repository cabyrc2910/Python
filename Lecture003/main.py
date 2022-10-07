## Анонимные, lambda функции
###################################################

# def sum(x):
#  return x+10
# sum = lambda x: x+10
# # def mult(x):
# #  return x**2
# mult = lambda x: x**2
# # sum(mult(2))

# # def sum1(x):
# #  return x+22
# sum1 = lambda x: x+22
# # def mult2(x):
# #  return x**3
# mult2 = lambda x: x**3
# # sum1(mult2(2))

# # def sum3(x):
# #  return x+242
# sum4 = lambda x: x+242
# # def mult4(x):
# #  return x**5
# mult4 = lambda x: x**5
# # sum3(mult2(2))

############################

# def f(x):
#     x**2
# g = f
# print(f(1))    #   вызываем  f  передаём туда аргументы
# print(g(21))   #    вызываем  g

##############################

# def f(x):
#     return x**2
# g = f
# # print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

###############################

# def calc1(x):
#     return x+10
# print (calc1(10))

# def calc2(x):
#     return x*10
# # print (calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

###############################
# пример функции с 2 переменными
###############################

# def sum(x, y):
#  return x+y

# sum = lambda x, y: x+y
# def mult(x, y):
#  return x*2

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
# calc(lambda x, y: x+y, 4, 5)

#################################

# sum = lambda x: x+10
# mult = lambda x: x**2
# sum(mult(2))

# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# sum1(mult2(2))

# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# sum3(mult2(2))

# f(g(x))
# def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))
# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)

###################################################
## List Comprehension
###################################################

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#############################

# list = []
# for i in range(1, 21):
#     # if (i%2==0):
#         list.append(i);

# print(list)     # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# list = [i for i in range(1, 11)]   
# print(list)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# list = [(i, i) for i in range(1, 7) if i % 2 == 0]
# print(list)  #  кортеж  [(2, 2), (4, 4), (6, 6)]

# def f(x):
#     return x**3
# list = [f(i) for i in range(1, 11) if i % 2 == 0]
# print(list)  #  [8, 64, 216, 512, 1000]

# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 11) if i % 2 == 0]
# print(list)  #  кортеж [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000)]

############################
#  В файле хранятся числа, 
# нужно выбрать четные и составить список пар (число; квадрат числа). 
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]
############################

path ='/Users/Иван/Desktop/GeekBrains/Python/Lecture003/file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != ' ':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)