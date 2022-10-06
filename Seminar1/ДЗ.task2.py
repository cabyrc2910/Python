# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

############################################################

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))
if not (x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False) 

###########################################################

# def CheckStatement():
#     count = 0
#     for x in range(2):
#         for y in range(2):
#              for z in range (2):
#                 rez = (not(x or y or z) ==((not x) and (not y) and (not z)))
#                 print(rez)
#                 if rez: count += 1     # Если результат истина то счётчик прибавляем
#                 else: print('Утверждение не верно')
#     if count == 8: print('Утверждение верно')     # 8 - это 2 в степени 3 - столько возможно комбинаций
# CheckStatement()           