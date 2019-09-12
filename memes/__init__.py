import logging
import json
from handlers import start_handler, echo_handler, meme_handler, random_handler, help_handler
from telegram.ext import Updater

with open('./../config.json', 'r') as f:
    config = json.load(f)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
updater = Updater(token=config['TOKEN'], use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(meme_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(help_handler)

updater.start_polling()