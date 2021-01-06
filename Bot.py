import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("bot is ready.")

client.run('Nzk2MjU2ODA3NjM4NTMyMTE3.X_VR8A.uY-K0oQnSmkOW2dOmfE0V4XX_I0')
