import discord
import os
from discord.ext import commands
# some_file.py
import sys
sys.path.append("./info")

import pokedexDatabase


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
map_array = ["Pallet Town", "Route 1", "Viridian City", "Route 2", "Viridian Forest", "Pewter City", "Route 3", "Mt. Moon", "Route 4", "Cerulean City", "Route 5"]
origin = "Pallet Town"
back = ""
forward = ""
two_forward = ""

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'Pokedex.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Pokedex.{extension}')

@client.command()
async def location(ctx):
    await ctx.send(f'Your location is: {origin}')

@client.command()
async def move(ctx):
    global back, forward, two_forward
    for i in range(len(map_array)):
        if map_array[i] == origin:
            if i == 0:
                forward = map_array[i + 1]
                two_forward = map_array[i + 2]
                back = map_array[i]
            elif i == (len(map_array) - 1):
                back = map_array[i - 1]
                forward = map_array[0]
                two_forward = map_array[1]
            elif i == (len(map_array) - 2):
                forward = map_array[i + 1]
                back = map_array[i - 1]
                two_forward = map_array[0]
            else:
                forward = map_array[i + 1]
                two_forward = map_array[i + 2]
                back = map_array[i - 1]
    await ctx.send(f'```You can go:\n1. {forward}\n2. {back}\n3. {two_forward}```')

@client.command()
async def go(ctx, response : str):
    global origin, forward, two_forward, back
    print(origin)
    print(forward)
    if response == forward:
        origin = forward
        await ctx.send(f'you are now in {origin}')
    elif response == two_forward:
        origin = two_forward
        await ctx.send(f'you are now in {origin}')
    elif response == back:
        origin = back
        await ctx.send(f'you are now in {origin}')
    else:
        await ctx.send(f'Cannot travel there at this time.')


for filename in os.listdir('./Pokedex'):
    if filename.endswith('.py'):
        client.load_extension(f'Pokedex.{filename[:-3]}')

client.run('Nzk2MjU2ODA3NjM4NTMyMTE3.X_VR8A.rbRYxXigvbHg2GX4nuoZDJ_MY9M')
