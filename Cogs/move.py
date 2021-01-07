import discord
from discord.ext import commands

class move(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("working!")

    @commands.command()
    async def working(self, ctx):
        await ctx.send(f'Working!!' )

def setup(client):
    client.add_cog(move(client))
