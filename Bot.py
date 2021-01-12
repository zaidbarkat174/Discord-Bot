import discord
import os
import random
from discord.ext import commands
# some_file.py
import sys
sys.path.append("./info")

import pokedexDatabase


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
map_array = ["Pallet Town", "Route 1", "Viridian City", "Route 2", "Viridian Forest", "Pewter City", "Route 3", "Mt. Moon", "Route 4", "Cerulean City", "Route 5"]
origin = "Pallet Town"
object = ""
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
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.bot.logout()
    await login("Nzk1NDMyMjg4MDgyOTg0OTcx.X_JSCw.szQQ8yQhbOAuP9mPYLDZA", bot=True)

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

@client.command()
async def search(ctx):
    global object
    if origin == "Route 1":
        route_1_chances = 5, 5
        route_1_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[18].name
        route_1_dic = {}
        for val in pokedexDatabase.pokemon_array:
            route_1_dic[val.name] = val
        route_1 = [v for v, d in zip(route_1_pokemon, route_1_chances) for i in range(d)]
        for i in range(1):
            pokemon = random.choice(route_1)
            object = route_1_dic[pokemon]
            await ctx.send("You have encountered ***" + pokemon + "***! Do you want to try to catch it?")
    elif origin == "Route 2":
        route_2_chances = 15, 45, 40
        route_2_pokemon = pokedexDatabase.pokemon_array[12].name, pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[18].name
        route_2 = [v for v, d in zip(route_2_pokemon, route_2_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_2) + "***! Do you want to try to catch it?")
    elif origin == "Route 3":
        route_3_chances = 45, 45, 10
        route_3_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[38].name
        route_3 = [v for v, d in zip(route_3_pokemon, route_3_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_3) + "***! Do you want to try to catch it?")
    elif origin == "Route 4":
        route_4_chances = 40, 35, 25
        route_4_pokemon = pokedexDatabase.pokemon_array[18].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[22].name
        route_4 = [v for v, d in zip(route_4_pokemon, route_4_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_4) + "***! Do you want to try to catch it?")
    elif origin == "Route 5":
        route_5_chances = 40, 35, 25
        route_5_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[55].name
        route_5 = [v for v, d in zip(route_5_pokemon, route_5_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_5) + "***! Do you want to try to catch it?")
    elif origin == "Route 6":
        route_6_chances = 40, 35, 25
        route_6_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[55].name
        route_6 = [v for v, d in zip(route_6_pokemon, route_6_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_6) + "***! Do you want to try to catch it?")
    elif origin == "Route 7":
        route_7_chances = 30, 30, 30, 10
        route_7_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[55].name, pokedexDatabase.pokemon_array[57].name
        route_7 = [v for v, d in zip(route_7_pokemon, route_7_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_7) + "***! Do you want to try to catch it?")
    elif origin == "Route 8":
        route_8_chances = 35, 20, 25, 20
        route_8_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[22].name, pokedexDatabase.pokemon_array[55].name, pokedexDatabase.pokemon_array[57].name
        route_8 = [v for v, d in zip(route_8_pokemon, route_8_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_8) + "***! Do you want to try to catch it?")
    elif origin == "Route 9":
        route_9_chances = 40, 35, 25
        route_9_pokemon = pokedexDatabase.pokemon_array[18].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[22].name
        route_9 = [v for v, d in zip(route_9_pokemon, route_9_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_9) + "***! Do you want to try to catch it?")
    elif origin == "Route 10":
        route_10_chances = 30, 25, 45
        route_10_pokemon = pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[22].name, pokedexDatabase.pokemon_array[99].name
        route_10 = [v for v, d in zip(route_10_pokemon, route_10_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_10) + "***! Do you want to try to catch it?")
    elif origin == "Route 11":
        route_11_chances = 35, 40, 25
        route_11_pokemon = pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[22].name, pokedexDatabase.pokemon_array[95].name
        route_11 = [v for v, d in zip(route_11_pokemon, route_11_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_11) + "***! Do you want to try to catch it?")
    elif origin == "Route 12":
        route_12_chances = 35, 40, 5, 20
        route_12_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[43].name, pokedexDatabase.pokemon_array[47].name
        route_12 = [v for v, d in zip(route_12_pokemon, route_12_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_12) + "***! Do you want to try to catch it?")
    elif origin == "Route 13":
        route_13_chances = 35, 40, 5, 20
        route_13_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[43].name, pokedexDatabase.pokemon_array[47].name
        route_13 = [v for v, d in zip(route_13_pokemon, route_13_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_13) + "***! Do you want to try to catch it?")
    elif origin == "Route 14":
        route_14_chances = 15, 5, 40, 5, 20, 15
        route_14_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[16].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[43].name, pokedexDatabase.pokemon_array[47].name, pokedexDatabase.pokemon_array[131].name
        route_14 = [v for v, d in zip(route_14_pokemon, route_14_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_14) + "***! Do you want to try to catch it?")
    elif origin == "Route 15":
        route_15_chances = 15, 5, 40, 5, 20, 15
        route_15_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[16].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[43].name, pokedexDatabase.pokemon_array[47].name, pokedexDatabase.pokemon_array[131].name
        route_15 = [v for v, d in zip(route_15_pokemon, route_15_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_15) + "***! Do you want to try to catch it?")
    elif origin == "Route 16":
        route_16_chances = 30, 5, 40, 25
        route_16_pokemon = pokedexDatabase.pokemon_array[18].name, pokedexDatabase.pokemon_array[19].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[83].name
        route_16 = [v for v, d in zip(route_16_pokemon, route_16_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_16) + "***! Do you want to try to catch it?")
    elif origin == "Route 17":
        route_17_chances = 30, 40, 5, 25
        route_17_pokemon = pokedexDatabase.pokemon_array[19].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[21].name, pokedexDatabase.pokemon_array[83].name
        route_17 = [v for v, d in zip(route_17_pokemon, route_17_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_17) + "***! Do you want to try to catch it?")
    elif origin == "Route 18":
        route_18_chances = 20, 40, 15, 25
        route_18_pokemon = pokedexDatabase.pokemon_array[19].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[21].name, pokedexDatabase.pokemon_array[83].name
        route_18 = [v for v, d in zip(route_18_pokemon, route_18_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_18) + "***! Do you want to try to catch it?")
    elif origin == "Route 19":
        route_19_chances = 1
        route_19_pokemon = pokedexDatabase.pokemon_array[71].name
        route_19 = [v for v, d in zip(route_19_pokemon, route_19_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_19) + "***! Do you want to try to catch it?")
    elif origin == "Route 20":
        route_20_chances = 1
        route_20_pokemon = pokedexDatabase.pokemon_array[71].name
        route_20 = [v for v, d in zip(route_20_pokemon, route_20_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_20) + "***! Do you want to try to catch it?")
    elif origin == "Route 21":
        route_21_chances = 25, 15, 35, 15, 10
        route_21_pokemon = pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[16].name, pokedexDatabase.pokemon_array[18].name, pokedexDatabase.pokemon_array[19].name, pokedexDatabase.pokemon_array[113].name
        route_21 = [v for v, d in zip(route_21_pokemon, route_21_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_21) + "***! Do you want to try to catch it?")
    elif origin == "Route 22":
        route_22_chances = 45, 10, 5, 40
        route_22_pokemon = pokedexDatabase.pokemon_array[18].name, pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[28].name, pokedexDatabase.pokemon_array[31].name
        route_22 = [v for v, d in zip(route_22_pokemon, route_22_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_22) + "***! Do you want to try to catch it?")
    elif origin == "Route 23":
        route_23_chances = 15, 25, 25, 5, 30
        route_23_pokemon = pokedexDatabase.pokemon_array[20].name, pokedexDatabase.pokemon_array[21].name, pokedexDatabase.pokemon_array[22].name, pokedexDatabase.pokemon_array[33].name, pokedexDatabase.pokemon_array[131].name
        route_23 = [v for v, d in zip(route_23_pokemon, route_23_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_23) + "***! Do you want to try to catch it?")
    elif origin == "Route 24":
        route_24_chances = 20, 20, 20, 25, 15
        route_24_pokemon = pokedexDatabase.pokemon_array[12].name, pokedexDatabase.pokemon_array[13].name, pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[62].name
        route_24 = [v for v, d in zip(route_24_pokemon, route_24_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_24) + "***! Do you want to try to catch it?")
    elif origin == "Route 25":
        route_25_chances = 1, 4, 20, 20, 15, 25, 15
        route_25_pokemon = pokedexDatabase.pokemon_array[9].name, pokedexDatabase.pokemon_array[10].name, pokedexDatabase.pokemon_array[12].name, pokedexDatabase.pokemon_array[13].name, pokedexDatabase.pokemon_array[15].name, pokedexDatabase.pokemon_array[42].name, pokedexDatabase.pokemon_array[62].name
        route_25 = [v for v, d in zip(route_25_pokemon, route_25_chances) for i in range(d)]
        for i in range(1):
            await ctx.send("You have encountered ***" + random.choice(route_25) + "***! Do you want to try to catch it?")
    else:
        await ctx.send("This area contains no wild Pokemon")

@client.command()
async def catch(ctx, response : str):
    global object
    if response == "yes":
        n = random.randint(0, 255)
        if n > object.catch_rate:
            await ctx.send("The pokemon has broken free!")
        else:
            m = random.randint(0, 255)
            await ctx.send(f"You have caught {object.name}! Congratulations!")



for filename in os.listdir('./Pokedex'):
    if filename.endswith('.py'):
        client.load_extension(f'Pokedex.{filename[:-3]}')

client.run('Nzk1NDMyMjg4MDgyOTg0OTcx.X_JSCw.szQQ8yQhbOAuP9mRtdkZA')
