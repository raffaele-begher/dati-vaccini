from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import requests
import re
import load_data as ld

def main():
    updater = Updater('1705491726:AAGvoImm9eFR62VI5kkanuqyPKUKiaymksI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dati', dati))
    updater.start_polling()
    updater.idle()


def dati(update, context):
    ld.update_dataset()
    ld.set_styles()
    dati = ld.get_data()
    context.bot.send_message(update.message.chat_id, dati)
    context.bot.send_photo(update.message.chat_id, photo=open('vax-die.png', 'rb'))

if __name__ == '__main__':
    main()
