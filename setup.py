import logging
import os
import discord
import dotenv

dotenv.load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    unallowedcharacters = '._-!¡¿?'
    cinco = [5, 'cinco']
    uve = ['v', 'uve']

    fullmessage = message.content.lower()

    logging.info(f'{message.author}: {message.content}')

    for character in unallowedcharacters:
        fullmessage = fullmessage.replace(character, '')

    if message.author == client.user:
        return

    for c in cinco:
        if fullmessage.endswith(str(c)):
            response = 'por el culo te la hinco jefe te falta calle'
            logging.info(f'El bot, todo un capo: {response}')
            await message.channel.send(response)

    for v in uve:
        if fullmessage.endswith(str(v)):
            response = 'en tu culo me entretuve sobrino'
            logging.info(f'El bot, todo un capo: {response}')
            await message.channel.send(response)


client.run(os.getenv('TOKEN'))
