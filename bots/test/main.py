import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEIBUhkBXaN-OTl0BzbqVDLmZkT493egAACEwADwDZPE6qzh_d_OMqlLgQ')
    bot.send_photo(message.chat.id, 'https://www.freecodecamp.org/news/content/images/2022/09/jonatan-pie-3l3RwQdHRHg-unsplash.jpg')

@bot.message_handler(content_types=['text'])
def aaaa(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет')
    else:
        bot.send_message(message.chat.id, 'Сообщение не распознанно')
    
@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.chat.id, message.sticker.file_id)

   

bot.polling()
