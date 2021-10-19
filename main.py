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
    },
    {
        "line": "El que tengo aquí colgado mestre",
        "endsWith": [
            'ogado',
        ]
    },
    {
        "line": "La que te va a dar esta figura te la has comido",
        "endsWith": [
            'iesta',
        ]
    },
]

gifs = [
    {
        "words": [
            "vieja",
            "novia",
            "madre",
            "abuela",
            "hermana",
            "tía",
        ],
        "responses": [
            "Sí pero poca broma con la {word} de {author}",
            "https://tenor.com/view/jamie-oliver-reacted-holding-show-gif-11864011",
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

    for gif in gifs:
        for word in gif.get('words'):
            if word in fullmessage:
                for response in gif.get('responses'):
                    response = response.replace('{author}', str(message.author))
                    response = response.replace('{word}', word)
                    await message.channel.send(response)

client.run(os.getenv('TOKEN'))
