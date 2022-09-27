import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM('859b1a518fcd7ea438a7e1768bd99b4b', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("5515635064:AAEDEFxbIyGtftbVx59ER-SzO9CEAz49E4M", parse_mode=None)  # telegram bot name: https://t.me/CityWeatherBot


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = "In the city " + message.text + " now " + w.detailed_status + "\n"
    answer += "Тhe temperature is now " + str(temp) + "\n\n"

    if temp < 0:
        answer += 'It seems like its already winter outside🥶'
    elif 0 <= temp <= 20:
        answer += 'Its cold, its better to wear a jacket🧥'
    elif 21 <= temp <= 30:
        answer += 'Finally great weather🌞'
    elif temp > 30:
        answer += 'I do not advise going outside, it is very hot there🥵'

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
