import discord
import os
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
map_array = ["Pallet Town", "1", "Viridian City", "2", "Viridian Forest", "Pewter City", "3", "Mt. Moon", "4", "Cerulean City", "5"]
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
    await ctx.send(f'you can go {forward} or {back} or {two_forward}')

    @client.command()
    async def go(ctx, response : str):
        global origin
        if response == forward:
            origin = forward
        elif response == two_forward:
            origin = two_forward
        elif response == back:
            origin = back
        else:
            print("not the right choice!!")
        await ctx.send(f'you are now in {origin}')


for filename in os.listdir('./Pokedex'):
    if filename.endswith('.py'):
        client.load_extension(f'Pokedex.{filename[:-3]}')

client.run('Nzk2MjU2ODA3NjM4NTMyMTE3.X_VR8A.Gnbgi3hFUb_Dm5pz5QgCrJ12xEw')
