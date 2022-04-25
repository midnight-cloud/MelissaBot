import telebot
import Messages
from Values import API_KEY

melissa = telebot.TeleBot(API_KEY)

# /start command
@melissa.message_handler(commands=['start'])
def command_start(message):
    res = Messages.start_message(message.from_user.first_name)
    melissa.send_message(message.chat.id, res, parse_mode='html')


#start working bot
melissa.polling(none_stop=True)