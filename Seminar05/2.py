###################################################################################
# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастащую последовательность. Порядок элементов менять нельзя.
# Пример:[1, 5, 2, 3, 4, 6, 1, 7] -> [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
####################################################################################

from ast import Num


# num = [11, 5, 2, 3, 4, 6, 1, 7, 9, 8, 10]

# def nextmax(list):
#     max = list[0]
#     res = [list[0]]
#     for i in range(len(list)):
#         if list[i] > max:
#             max = list[i]
#             res.append(max)
#     if len(res)==1:
#         res = nextmax(list[1:])
#     return res

# print(nextmax(num))   #  [5, 6, 7, 9, 10]

##################################################

num = [11, 12, 2, 3, 4, 6, 1, 7, 9, 8, 10]

def nextmax(list):
    max = list[0]
    res = [list[0]]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            res.append(max)
    if len(res) < 3:
        res = nextmax(list[1:])
    return res

print(nextmax(num))   #  [2, 3, 4, 6, 7, 9, 10]