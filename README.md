# Memebot

A telegram meme bot, consuming data from knowyourmeme.com.
Demo: @tipos_de_carinhas_sao_bot in telegram.

![meme](https://i.kym-cdn.com/entries/icons/original/000/000/063/Rage.jpg)

# Host it yourself!

It's extremely ease to host this bot if you have a VPS or you can even run it in your computer. Just be sure that you have [python3](https://www.python.org/downloads/) and [poetry](https://github.com/sdispater/poetry) installed.

### Clone the repo

```
git clone https://github.com/leviosar/memebot.git
```

### Enter in the directory and run poetry

```
cd memebot
poetry install
```

### Add your bot's token

You can get a token for a bot from @BotFather on Telegram, if you already have yours just create a config.json with the following pattern

```json
{
    "TOKEN": "mytoken"
}
```

### Running script

You can simply run ```python ./memes/__init__.py``` but the bot will stop if you close your terminal, to run it in background i suggest using ```nohup```.

```
nohup ./memes/__init__.py &
```

# Commands

#### /random

Send a random meme pic from /r/memes

#### /def :meme_string

Send the first result of www.knowyourmeme.com from searching :meme_string parameter.