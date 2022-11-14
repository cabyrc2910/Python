from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import *


app = ApplicationBuilder().token('5483049801:AAEf7i1v5IETsrx0pP4dUfsWJ9joeI_R-jo').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("diff", diff_command))
app.add_handler(CommandHandler("multi", multi_command))
app.add_handler(CommandHandler("div", div_command))
print('server start')
app.run_polling()
