from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/sum\n/diff\n/multi\n/div')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} - {y} = {x-y}')


async def multi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')


async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x} / {y} = {x/y}')
