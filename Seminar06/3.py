########################################################################################
# Написать функцию, аргументы имена сотрудников , возвращает словарь первая буква ключ,
#  значения это список содержащий имена на эту букву
########################################################################################

from collections import Counter

input_names = ["Иван", "Мария", "Петр", "Илья",
               "Марина", "Петр", "Алина", "Бибочка"]


def sort_names(names: list):
    name_book = Counter()
    for name in names:
        if name[0] in name_book:
            name_book[name[0]].append(name)
        else:
            name_book[name[0]] = [name]
    return name_book


print(sort_names(input_names))

##################################################################

def employeeDic(names):
    names.sort()
    preKeys=[i[0] for i in names]
    keys=[]
    for i in range(len(preKeys)):
        if not preKeys[i] in keys:
            keys.append(preKeys[i])
    dic={}
    for i in range(len(keys)):
        dic[keys[i]]=[]
    for key in range(len(keys)):
        for name in range(len(names)):
            if names[name][0]==keys[key]:
                dic[keys[key]].append(names[name])
    return dic

names=input('Имена сотрудников, через запятую: ').split(',')
#names=["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

print(employeeDic(names))