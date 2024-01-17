# ONLY FROM AIOGRAM LIBARY

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ONLY STANDART PYTHON LIBARY

from random import randint
import asyncio

# ONLY PARSING LIBARY

from bs4 import BeautifulSoup
import requests
