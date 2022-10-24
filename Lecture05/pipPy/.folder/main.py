#####################################################
## Библиотека: isOdd
#####################################################

# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))

#####################################################
## Библиотека: prpgress
#####################################################

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

#####################################################
## Библиотека: emoji
#####################################################

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

#####################################################
## Библиотека: matplotlib
#####################################################

# import matplotlib.pyplot as plt
# import numpy as np

# list =[1,2,3,2,7]
# plt.plot(list, )

# plt.show()

#####################################################
## Библиотека: telegram
#####################################################

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater("5483049801:AAEf7i1v5IETsrx0pP4dUfsWJ9joeI_R-jo")

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


print('server start')
updater.start_polling()
updater.idle() 
