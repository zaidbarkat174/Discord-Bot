import discord
import os
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Pokedex.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Pokedex.{extension}')

for filename in os.listdir('./Pokedex'):
    if filename.endswith('.py'):
        client.load_extension(f'Pokedex.{filename[:-3]}')

client.run('Nzk2MjU2ODA3NjM4NTMyMTE3.X_VR8A.BmbfECQfPZ3njw909HYwr5wKWc0')
