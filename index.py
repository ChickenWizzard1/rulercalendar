import os
token = os.environ['TOKEN']
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rulercalendar.coolo2.repl.co/")
rc_time = driver.find_element(By.XPATH, "//span[@id='time-small']").text
#rc_time = "Rulercraft  time is:", rc_time
rl_time = driver.find_element(By.XPATH, "//span[@id='rl-time-small']").text
#rl_time =  "Real time is:", rl_time
print(rc_time)
print("In GMT:", rl_time)
time_command = driver.find_element(By.XPATH, "//span[@id='time-small']").text, driver.find_element(By.XPATH, "//span[@id='rl-time-small']").text, "in gmt"
help_command = "Do _time in the Afrea server to convert Rulercraft time to Realtime"
import discord

from discord.ext import commands

from webserver import keep_alive

client = commands.Bot(command_prefix = "_")

client.remove_command('help')

@client.event

async def on_ready():

    print("Bot is currently online!")


    #help command

    @client.command(pass_context=True)

    async def help(ctx):

        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Colour.orange()

        )

        embed.set_author(name="Help")

        embed.add_field(name="Help", value=help_command, inline=False)

        channel = await author.create_dm()

        await channel.send(author,embed=embed)

        await ctx.message.channel.send(author,embed=embed)

    @client.command(pass_context=True)

    async def time(ctx):

        author = ctx.message.author

        embed = discord.Embed(

            colour = discord.Colour.orange()

        )
        embed.set_author(name="Whats the time?")

        embed.add_field(name="Whats the time in RC / Realtime?", value=time_command, inline=False)

        channel = await author.create_dm()

        await channel.send(author,embed=embed)

        await ctx.message.channel.send(author,embed=embed)


keep_alive()

TOKEN = os.environ['TOKEN']

client.run(TOKEN)
