import discord
import yfinance as yf
from discord import Intents
from discord.ext.commands import Bot
intent = Intents().all()
bot = Bot(command_prefix='prefix', intents=intent)
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!m', intents=intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    await bot.change_presence(
    activity = discord.Activity(type=discord.ActivityType.playing, name='!m(help) & Yahoo Finance API'))
    print('Bot is online & running!')
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))



@bot.event
async def on_member_join(member):
   await bot.get_channel(insert channel id here as an integer).send(f"Welcome, {member.name}!")

@bot.event
async def on_member_remove(member):
   await bot.get_channel(insert channel id here as an integer).send(f"Farewell, {member.name}!")


@bot.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use !mhelp for extended information.", color = ctx.author.color)
    em.add_field(name = "Stock Price", value = "!m -insertticker-")
    await ctx.send(embed = em)


@help.command()
async def ticker(ctx):
    em = discord.Embed(title = "Stock Price", description = "Displays the Current Stock Price with a Ticker.", color = author.ctx.color)
    em.add_field(name = "**Syntax**", value = "!m-ticker-")
    await ctx.send(embed = em)


@bot.command()
async def ping(ctx):
    await ctx.send(f'Here is your ping: {round(bot.latency * 1000)}ms')


@bot.command(aliases=[''], help='!m"insert ticker here"')
async def price(ctx, args):
    ticker = args.upper()
    data = yf.download(tickers=ticker, period='1d')
    last_price = data['Close'][0]
    await ctx.send("The last price of {} was ${:.2f}".format(ticker, last_price))


bot.run('insert bot id here')
