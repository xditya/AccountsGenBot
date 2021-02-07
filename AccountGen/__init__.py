#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/xditya/AccountsGenBot/blob/master/LICENSE > 
#    for the license.

from telethon import TelegramClient
from decouple import config
import logging
import time
import redis

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
ACCOUNTS = config("ACCOUNTS", default=None)
CHANNEL = config("CHANNEL", default=None)
START_MSG = config("START", default=None)
ACC_NAME = config("ACC_NAME", default=None)
OWNER_ID = config("OWNER_ID", default=None)
# Redis
REDIS_URI = config("REDIS_URI", default=None)
REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)

BotzHub = TelegramClient('BotzHub', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

try:
    redis_info = REDIS_URI.split(':')
    xdi = redis.StrictRedis(
    host=redis_info[0],
    port=redis_info[1],
    password=REDIS_PASSWORD,
    charset="utf-8",
    decode_responses=True)
except Exception as e:
    print("Database errors! Recheck REDIS_URI and REDIS_PASSWORD!!")
    print(str(e))
    print("Bot is quiting...")
    exit()
