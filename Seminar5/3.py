#############################################################################
# Напишите программу, удаляющую из текста все слова, содержащие ""abc"".
#############################################################################

input_string = "sdfsdf abc asdf asdfabc sdfsabc asdfsdfasd ljklkj asdfsadf"
remove_word = "abc"

temp_list = list(filter(lambda x: remove_word not in x, input_string.split()))
print(" ".join(temp_list))

#############################

text_my = 'Напишите программуabc , удаляющуюabc из текста все словаabc, содержащие "abc"'

text_my = list(filter(lambda x: 'abc' not in x, text_my.split()))
my = " ".join(text_my)
print(my)