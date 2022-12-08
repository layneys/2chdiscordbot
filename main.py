import requests, discord, os
from bs4 import BeautifulSoup
from random import randint

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pasta'):
        random_num = randint(1, 520)

        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
        }

        url = f"https://pastach.ru/p/{random_num}"

        req = requests.get(url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")

        paste = soup.find(class_="paste-content")
        await message.channel.send(f'{paste.txt}')

client.run(os.getenv('ахаха здесб ничего нет'))
