#############################################################################
#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах
#############################################################################

# def unzip(compressed_string:str):
#     new_string = ""
#     digit = ""
#     for i in range(len(compressed_string)):
#         if compressed_string[i].isdigit():
#             digit += compressed_string[i]
#         else:
#             new_string += compressed_string[i] * int(digit)
#             digit = ""
            
#     return new_string
        
    
# def rle2(string: str):
#     new_string = ""
#     last_symmbol = string[0]
#     count = 1
    
#     for i in range(1, len(string)):
#         if string[i] == last_symmbol:
#             count += 1
#             continue
#         else:
#             new_string += f"{count}{last_symmbol}"
#             last_symmbol = string[i]
#             count = 1
            
#     new_string += f"{count}{last_symmbol}"
    
#     return new_string

# in_string = "wwwwwwwwwwwwwwasdasdasdasdasdasdoooooooqweqwadaaaaaaaa"
# print(in_string)
# compressed = rle2(in_string)
# print(compressed)
# unpack = unzip(compressed)
# print(unpack)
# print(unpack == in_string)

###########################################################################

# import os
# os.system("cls")


# def write_file(name, st):
#     with open(name, 'w') as data:
#         data.write(st)


# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-3):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-6] != txt[-5]):
#         res = res + str(count) + txt[-1]
#     return res


# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# print('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW\n')
# s = write_file('Seminar5\ДЗ.task4.file1.txt', input("Введите текст для кодировки: "))
# with open('Seminar5\ДЗ.task4.file1.txt', 'r') as data:
#     file1 = (" ".join(data.readlines()))
# d = write_file('Seminar5\ДЗ.task4.file2.txt', coding(file1))
# with open('Seminar5\ДЗ.task4.file2.txt', 'r') as data:
#     file2 = (" ".join(data.readlines()))
# print(f"Текст после кодировки: {coding(file1)}")
# print(f"Текст после дешифровки: {decoding(file2)}")

######################################################################################

data1 = open('Seminar5\ДЗ.task4.file1.txt', 'r')
myData = []
for line in data1:
    myData.extend(line)
data1.close()
print(myData)
count = 1
myNewData = []
for index in range(1, len(myData)):
    if myData[index -1] == myData [index] and index != len(myData)-1:
        count += 1
    elif myData[index -1] != myData[index] and index != len(myData)-1:
        myNewData.append(count)
        myNewData.append(myData[index-1])
        count = 1
    elif index ==len(myData)-1:
        count += 1
        myNewData.append(count)
        myNewData.append(myData[index])
print(''.join(map(str, myNewData)))
with open('Seminar5\ДЗ.task4.file2.txt', 'w') as data2:
    data2.write(''.join(map(str, myNewData)))