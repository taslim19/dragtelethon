import os
import logging

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from pytgcalls import PyTgCalls  

from Config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

BOT_USERNAME = Config.BOT_USERNAME
ASSISTANT_ID = Config.ASSISTANT_ID

bot = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)
Zaid = bot.start(bot_token=Config.BOT_TOKEN)

client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
call_py = GroupCallFactory(client).get_group_call()  # ✅ Correct initialization

client.start()
call_py.start()
