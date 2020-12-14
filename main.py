import discord 
import time
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
from Modules.Help import *
from Modules.ImageSearch import *

token = ""
game = discord.Game("Developing...")

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    await bot.change_presence(status= discord.Status.idle, activity=game)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 명령어(ctx):
    help = Help()
    CommandEmbed = help.Create_help_embed()
    await ctx.send(embed=CommandEmbed)

@bot.command()
async def 모야(ctx):
    help = Help()
    Description = help.Create_Moya_description()
    await ctx.send(embed=Description)
    
@bot.command()
async def 이미지(ctx, arg):
    search = Search()
    await ctx.send(embed=search.Search_Image(arg))

bot.run(token)