import telebot
from decouple import config

token = config('TOKEN')

# stickery
yes_sticker = 'CAACAgIAAxkBAAEIBUhkBXaN-OTl0BzbqVDLmZkT493egAACEwADwDZPE6qzh_d_OMqlLgQ'
no_sticker = 'CAACAgIAAxkBAAMcZAV9992FdbY79HMhtPAi_pJGB4MAAgkAA8A2TxPvzRuiSv9xlS4E'
bot = telebot.TeleBot(token)

# klaviatura
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('Да')
b2 = telebot.types.KeyboardButton('Нет')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, no_sticker)
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')

    bot.register_next_step_handler(message, reply_to_button) # jdet sleduyushego soobshenya



bot.polling()
