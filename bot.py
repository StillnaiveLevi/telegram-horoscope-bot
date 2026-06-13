import os
from dotenv import load_dotenv
load_dotenv()
import telebot
import requests

token = os.environ.get('token')  

bot = telebot.TeleBot(token)


def get_daily_horscope(sign: str, day: str)-> dict:
    """Get daily horscope for your zodiac sign.
    keyword arguments:
    sign:str- your sign
    day:str-date in yyyy-mm-dd or today or tommorow or yesterday
    return:dict:json data"""
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params ={"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text:"What's your zodiac sign?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    sign = message.text
    text = "what day you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")