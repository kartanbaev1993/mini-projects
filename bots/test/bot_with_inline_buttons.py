import telebot
from decouple import config

token = config('TOKEN')

# stickery
yes_sticker = 'CAACAgIAAxkBAAEIBUhkBXaN-OTl0BzbqVDLmZkT493egAACEwADwDZPE6qzh_d_OMqlLgQ'
no_sticker = 'CAACAgIAAxkBAAMcZAV9992FdbY79HMhtPAi_pJGB4MAAgkAA8A2TxPvzRuiSv9xlS4E'

# klaviatura pod soobsheniem
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1, b2)



bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)

    #func - funkciya filtr v dannom sluchae razreshayutsya vse soobsheniya
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_sticker)



bot.polling()