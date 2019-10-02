import memedict
import requests
import json
from responses import HELP_MESSAGE

log_memes = list()

def recover_log(log):
    with open('./logs/memes.json', 'r') as f:
        log = json.load(f)

recover_log(log_memes)

def start(update, context):
    """ Fired on bot start """
    context.bot.send_message(chat_id=update.message.chat_id, text="Memes, tipos de carinhas são")

def echo(update, context):
    """ Default wtf response to all non-command """
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/IIF96Bb.jpg')

def definition(update, context):
    """ Use memedict package to search for a meme definition in know your meme """
    needle = ' '.join(context.args)
    add_to_log(needle, 'def', context.user_data)
    result = memedict.search(needle)
    if result is not None:
        context.bot.send_message(chat_id=update.message.chat_id, text=result)
    else:
        context.bot.send_photo(chat_id=update.message.chat_id, photo='https://i.imgur.com/IIF96Bb.jpg')

def random(update, context):
    """ Use meme-api to fetch a random meme from /r/meme """
    meme = requests.get('https://thememapi.online/image/random')
    meme = meme.json()
    add_to_log(meme, 'random', context.user_data)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=meme['src'])

def handler_help(update, context):
    """Send a message when the command /help is issued."""
    context.bot.send_message(chat_id=update.message.chat_id, text=HELP_MESSAGE)

def add_to_log(search, command, user):
    dump = {'search': search, 'command': command, 'user': user}
    log_memes.append(dump)
    with open('./logs/memes.json', 'w') as output_file:
        json.dump(log_memes, output_file)

