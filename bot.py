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