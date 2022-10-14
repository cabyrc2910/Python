############################################################################
#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
############################################################################
import os
os.system("cls")

my_text = 'ываабв лповап абвцукв алоабвабв ываываыв'
my_text = filter(lambda x: 'абв' not in x, my_text.split())
new_text = " ".join(my_text)
print(new_text)

###############################################################################

# my_text = 'оафвену драбвмлдт йемпаывпимдоа щдшабвуроа шгкупрг'
# print(my_text)

# my_list = my_text.split()
# print(my_list)

# for item in my_list:
#     if 'абв' in item:
#         my_list.remove(item)

# print(my_list)

################################################################################

# import random
# # generate random words from syllables
# syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
# print(random.sample(syllables, 2))
# text = list(map(lambda x: "".join(random.sample(syllables, 3)),
#             range(random.randint(12, 15))))
# print(f' TEXT : {" ".join(text)}')
# print(*text)
# # search for syllable "абв" and delete it with whole word
# parsed_text = list(x for x in text if "абв" not in x)
# print(f'PARSED: {" ".join(parsed_text)}')

#################################################################################

# my_text = 'Напишите программу, удаляющую из текста все слова, содержащие "абв".'
# my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
# my = " ".join(my_text)
# print(my)