# imports:
import asyncio
import packages_needed
need_install_package = True
if (need_install_package):
  packages_needed.pip_install("discord.py")
  packages_needed.pip_install("flask")
import discord
import random
import os # (For loading all COGS extension module)
from discord.ext import commands
import keep_alive
#-------------------------------
# Bot setup:
bot = commands.Bot(command_prefix= 'n.')
# client = discord.Client()
# bot_token_id = os.getenv("DISCORD_BOT_SECRET")

print('Input token:')
bot_token_id = input()


# This function is inside cogs folder
# @bot.event
# async def on_ready(): # Put bot in ready state
#     print('Bot is ready.')
#     print('Login as {0.user}'.format(bot))

# Welcome message when members join a server:
@bot.event
async def on_member_join(member):
    print(f'Welcome to the server, my nigga {member}')

# Message when member leaves a server!
@bot.event
async def on_member_remove(member):
    print(f"This nigga {member} left the server meanwhile everyone here is sucking {member}'s mum")
    
@bot.event
async def on_guild_role_create(role):
    print(f'The role {role} has been created!!')

# Use bot commands:
@bot.command()
async def plshelp(ctx): # pass context in this function argument
    await ctx.send('Shut the fuck up retard!')

#Check bot latency:    
@bot.command()
async def ping(ctx):
    await ctx.send(f'Bot latency: {round(bot.latency * 1000)}ms; ({round(bot.latency,2)}s)')

@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, user_question): # use '8ball user_question in discord cmd'
    responses = [
                    "It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."
    ] 
    # needs import random for RNG :))
        # do: random.choice(vars_array) to get start
    chosen_response = random.choice(responses)
    await ctx.send(f'Your question: {user_question}\nAnswer: {chosen_response}')

# Purge chat channel
@bot.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)

@bot.command()
async def kick(ctx, user_to_kick : discord.Member, *, the_reason = None):
    await user_to_kick.kick(reason = the_reason)
    await ctx.send(f'**User** {user_to_kick} is kicked!')
    await ctx.send(f'**Reason:** {the_reason}')
    
    
@bot.command()
async def ban(ctx, user_to_ban : discord.Member, *, the_reason = None):
    await user_to_ban.ban(reason = the_reason)
    await ctx.send(f'**This dumb nigga** {user_to_ban} had been banned\n**Reason:** {the_reason}')

@bot.command()
async def unban(ctx, *, unban_member):
  member_name, member_discriminator = unban_member.split('#')
  
  banned_users = await ctx.guild.bans() # get list of ban entries in the server
  for ban_entry in banned_users:
    user_to_unban = ban_entry.user

    if (user_to_unban.name, user_to_unban.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user_to_unban)
      await ctx.send(f'**Unbanned** {user_to_unban.name}#{user_to_unban.discriminator}')
      return

@bot.command()
async def user_id(ctx, *, input_name:discord.User):
  user_name_input = input_name.name
  member_id = input_name.id
  user_avatar = input_name.default_avatar
  await ctx.send(f"User id of {user_name_input}: {member_id}")

# COGS
# Load COGS' extension command:
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}') # Go into 'cogs' folders and load all .py extension
    await ctx.send(f"{extension} cog is loaded!")

# Unload COGS' extension command:
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unload {extension} cog!")

# Reload COGS (to refresh it)!
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} is reloaded!")


cogs_folder = './cogs'

for filename in os.listdir(cogs_folder):
    # Loop all files in that cogs_folder directory:
    if filename.endswith('.py'): # All files end with filetype '.py'
        bot.load_extension(f'cogs.{filename[:-3]}') # Load cogs file but don't take ".py" as its name

keep_alive.keep_alive()
bot.run(bot_token_id, bot=True, reconnect=True)