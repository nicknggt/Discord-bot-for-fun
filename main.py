# imports:
import asyncio
import packages_needed
is_install_package = False
if (is_install_package):
  packages_needed.install_packages()
import discord
import random
import os
from discord.ext import commands
import keep_alive
#-------------------------------
# Bot setup:
bot = commands.Bot(command_prefix= 'n.')
# client = discord.Client()
# bot_token_id = os.getenv("DISCORD_BOT_SECRET")

print('Input token:')
bot_token_id = input()



@bot.event
async def on_ready(): # Put bot in ready state
    print('Bot is ready.')
    print('Login as {0.user}'.format(bot))

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
  banned_users = await ctx.guild.bans() # get list of ban entries in the server
  member_name, member_discriminator = unban_member.split('#')

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






keep_alive.keep_alive()
bot.run(bot_token_id, bot=True, reconnect=True)