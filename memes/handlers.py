from telegram.ext import CommandHandler, MessageHandler, Filters
from functions import start, echo, definition, random, handler_help

start_handler = CommandHandler('start', start)
meme_handler = CommandHandler('def', definition)
echo_handler = MessageHandler(Filters.text, echo)
random_handler = CommandHandler('random', random)
help_handler = CommandHandler('help', handler_help)