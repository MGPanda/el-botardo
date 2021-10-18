import logging
import os
import discord
import dotenv

dotenv.load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    unallowedcharacters = '._-!¡¿?'
    cinco = [5, 'cinco']
    uve = ['v', 'uve']

    fullmessage = message.content.lower()

    for character in unallowedcharacters:
        fullmessage = fullmessage.replace(character, '')

    if message.author == client.user:
        return

    for c in cinco:
        if fullmessage.endswith(str(c)):
            print(f'{message.author}: {message.content}')
            response = 'por el culo te la hinco jefe te falta calle'
            print(f'El bot, todo un capo: {response}')
            await message.channel.send(response)

    for v in uve:
        if fullmessage.endswith(str(v)):
            print(f'{message.author}: {message.content}')
            response = 'en tu culo me entretuve sobrino'
            print(f'El bot, todo un capo: {response}')
            await message.channel.send(response)


client.run(os.getenv('TOKEN'))
