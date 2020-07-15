import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('8d79698cc4b916d8b3078060dec62244', config_dict)
bot = telebot.TeleBot('1180639658:AAEdsfpwkb3N3_oBXrgC0OpvsQzY_vp_4cM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет.Назови город в котором хочешь узнать погоду')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я скажу какая погоду в городе, тебе необходимо написать его название')

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        plase = message.text
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(plase)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        if temp<-20:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице мороз, лучше остаться дома')
        elif temp<0:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице холодно, одевайтесь теплее')
        elif temp<10:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице прохладно')
        elif temp<20:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице довольно тепло')
        elif temp<30:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице очень тепло')
        elif temp<40:
            bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас ' + w.detailed_status + "\n" 'Темература ' + str(temp) + "+С\n" 'на улице жарко')
        else:
            bot.send_message(message.chat.id, 'На улице аномальная жара')
    except:
        bot.send_message(message.chat.id,'Ошибка! Город не найден.') 
bot.polling(none_stop=True)

