import discord
from discord.ext import commands

# to make this work inside discord chat, simply do this before using any of these cmds:
# n.load example

class Example(commands.Cog): # this class inherits commands.Cog
    
    # Constructor:
    def __init__(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener() # This decoration allows to create event in COGS
    async def on_ready(self):
        print('Bot is online!')
    
    # Commands:
    @commands.command()
    async def ping_cog(self, ctx):
        await ctx.send(f'Bot latency: {round(commands.latency * 1000)}ms; ({round(commands.latency,2)}s)')
    


# Connect this COG to our bot function:
def setup(client):
    client.add_cog(Example(client))
    