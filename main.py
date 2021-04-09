import discord 
import time, os

from random import choice
from random import randint

from discord.ext import commands, tasks
from bs4 import BeautifulSoup

from Modules.Help import *
from Modules.ImageSearch import *
from Modules.Bitcoin import *

token = ""
game = discord.Game("Developing...")
prefix = "#"




bot = commands.Bot(command_prefix='#', description="Moyabot Developing..")

@bot.event #봇 실행.
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'{bot.user} is connected to the following:\n')

    for guild in bot.guilds:
        print(f'{guild.name}(id: {guild.id})')

    activity = discord.Activity(type=discord.ActivityType.watching, name="캬루")
    await bot.change_presence(activity=activity)


#누군가 들어왔을 때.
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi! {member.name}, welcome to Moya World!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')


###

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


@bot.command()
async def roll(ctx, min = 0, max= 100):
    if not(isint(max) and isint(min)):
        await ctx.send("숫자를 입력해주세요.")
        return 
    if max > 100000000000 or max < 1:
        await ctx.send("허용되지 않는 숫자범위입니다.")
        return 
    if min >= max:
        await ctx.send("최소값이 최대값보다 높거나 같게 설정되어 있습니다.")
        return
    
    await ctx.send(random.randint(min,max))
    


###

@bot.command(name='명령어')
async def 명령어(ctx):
    help = Help()
    CommandEmbed = help.Create_help_embed()
    await ctx.send(embed=CommandEmbed)

@bot.command(name='모야')
async def 모야(ctx):
    help = Help()
    Description = help.Create_Moya_description()
    await ctx.send(embed=Description)
    
@bot.command(name='이미지')
async def 이미지(ctx, arg):
    search = Search()
    await ctx.send(embed=search.Search_Image(arg))

@bot.command(name='업비트')
async def 업비트(ctx, *arg):
    Coinclass = get_coin()
    await ctx.send(embed=Coinclass.get_coin_price(*arg))

@bot.command()
async def 고르기(ctx, *choices):
    choices = [c for c in choices]
    if len(choices) < 2:
        await ctx.send("항목이 없습니다.")
    else:
        await ctx.send(choice(choices))
bot.run(token)