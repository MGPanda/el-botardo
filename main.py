import os
import discord
import dotenv

dotenv.load_dotenv()

client = discord.Client()

unallowedcharacters = '._-!¡¿?"\'()'

rimas = [
    {
        "line": "Por el culo te la hinco jefe te falta calle",
        "endsWith": [
            5,
            'inco',
            'inko',
        ]
    },
    {
        "line": "En tu culo me entretuve chaval venga a estudiar",
        "endsWith": [
            'v',
            'uve',
        ]
    }
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    fullmessage = message.content.lower()

    for character in unallowedcharacters:
        fullmessage = fullmessage.replace(character, '')

    if message.author == client.user:
        return

    for rima in rimas:
        for ew in rima.get('endsWith'):
            if fullmessage.endswith(str(ew)):
                print(f'{message.author}: {message.content}')
                print(f'El bot, todo un capo: {rima.get("line")}')
                await message.channel.send(rima.get('line'))


client.run(os.getenv('TOKEN'))
