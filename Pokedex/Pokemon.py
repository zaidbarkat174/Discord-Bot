import discord
from discord.ext import commands

class Pokemon(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("working_Pokemon file!")


def setup(client):
    client.add_cog(Pokemon(client))
