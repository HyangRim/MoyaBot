import discord 
import time, os,asyncio
import youtube_dl

from random import choice
from random import randint

from discord.ext import commands, tasks
from bs4 import BeautifulSoup

from Modules.Help import *
from Modules.ImageSearch import *
from Modules.Bitcoin import *
#from Modules.Music import *

token = "NTQzMDU5MTkyMjE1MjQwNzI1.XFwxSA.sFJS4E9wqEh0_XIivMJIjkwVpOg"
game = discord.Game("Developing...")
prefix = "#"

###

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source,volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()


    @commands.command()
    async def play(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        
        await ctx.send(f'Now playing: {player.title}')

###


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



###

bot.add_cog(Music(bot))



###
bot.run(token)