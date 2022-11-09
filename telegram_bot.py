
# Telegram bot 

import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


token = '5477511002:AAGHJYeaGWkg872u-2icVeyviRL889O4Iw8'
id = '885508103'
bot = telegram.Bot(token)
bot.send_message(chat_id=id, text='자도응답 테스트입니다, 말씀하세요.')

updater = Updater(token=token, use_context=True)
disbatcher = updater.dispatcher
updater.start_polling()

def handler(update,context):
    use_text = update.message.text
    if use_text == '안녕':
        bot.send_message(chat_id=id, text='안녕')
    if use_text == '지금 용업 중이신가요?':
        bot.send_message(chat_id=id, text='네 주문하시면 됩니다.')
    elif use_text == '네 알겠습니다. 지금 가겠습니다':
        bot.send_message(chat_id=id, text='네 조심해서 오세요.')
echo_hanler = MessageHandler(Filters.text, handler)
disbatcher.add_handler(echo_hanler)


