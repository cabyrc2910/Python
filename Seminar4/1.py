# Задайте строку из набора чисел. Напишите программу,которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

###################################################

nums = "1 2 3 4 67 5 6"
my_list = [int(num) for num in nums.split()]
print(max(my_list), min(my_list))

###################################################

def check_str(line):  # функция строку переводит в массив и проверяет чтобы там были только числа и отрицательные числа
    arr = line.split()
    for i in arr:
        if not i.strip("-").isdigit():
            return []
    return arr


def find_max_min(array):
    if array:
        # если несколько значений возвращаютс, то возвращается кортеж. key=int показывает что в стринге лежит число
        return min(array, key=int), max(array, key=int)
    return []


f = check_str("3 5 6 -10")
print(find_max_min(f))
