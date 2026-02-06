import discord
import config

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Connecté en tant que {self.user}!')

    async def on_message(self, message):
        print(f'Message recu de: {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config.TOKEN)
