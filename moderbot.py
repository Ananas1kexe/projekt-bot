import telebot
import webbrowser
from telebot import types

#token
bot = telebot.TeleBot('7111952552:AAHX_DhpO-wDTVy7Md-luME1b0LpnAWXFMY')

#commands
@bot.message_handler(commands=['youtube', 'ютуб'])
def site(message):
    webbrowser.open('https://www.youtube.com')

@bot.message_handler(commands=['google', 'гугл'])
def site1(message):
    webbrowser.open('https://www.google.com')

@bot.message_handler(commands=['автор'])
def site2(message):
    webbrowser.open('https://github.com/Ananas1kexe')

 
#слова для запуска 
@bot.message_handler(commands=['start', 'hello']) 
def main(message):
    bot.send_message(message.chat.id, f'привет!, {message.from_user.first_name} {message.from_user.last_name}')

#help information
@bot.message_handler(commands=['help']) 
def main(message):
    bot.send_message(message.chat.id, '''<b><u>Help information!</u></b>
напиши /start или /hello
/youtube чтобы открыть ютуб
/google чтобы открыть гугл
/автор чтобы открыть гитхаб автора
/создатель чтобы открыть ссылки на аккаунты автора''', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет!, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'создатель':
        bot.send_message(message.chat.id, ('''вот информация как поддержать автора
my github = https://github.com/Ananas1kexe
my discord = https://discord.gg/ZATnKgzcEK
my tg chanel = https://t.me/ananas1kexe
                                           '''))


@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup()
    btn4 = types.KeyboardButton('перейти на сайт')
    markup1.row(btn4)
    btn5 = types.KeyboardButton('Удалить фото')
    btn6 = types.KeyboardButton('Изменить текст')
    markup1.row(btn5, btn6)
    file = open('./jarvisdekstop.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup1)
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'перейти на сайт':
        bot.send_message(message.chat.id, 'website is open')
    elif message.text == 'удалить фото':
        bot.send_message(message.chat.id, 'deled')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт ', url='https://google.com')
    markup1.row(btn1) 
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup1.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup1)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



#run
bot.polling(non_stop=True)