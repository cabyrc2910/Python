# Для подготовки в к экзамену Рон каждый день учит x заклинаний, а гермиона на y заклинаний больше.
# Сколько заклинаний они выйчат вместе через n дней.
# В первой строке вводится x - количество заклинаний, которыке учит  Рон.
# Во второй строке y - на сколько заклинаний больше учит Гермиона.

#################################################################

r = int(input('Введите сколько заклинаний учит Рон X = '))
h = int(input('Введите на сколько заклинаний Гермиона учит больше чем Рон Y = ')) + r
n = int(input('Введите сколько дней учат заклинания Рон и Гермиона n = '))
res = (r + h)* n
print('Вместе они выучат', res, 'заклинаний')