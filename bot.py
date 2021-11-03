import discord
import random
import json
from discord.ext import commands

client = commands.Bot(command_prefix="$")

f = open('names.json', 'r')
names = json.load(f)

@client.event
async def on_ready():
    print("Bot is Online :)")


@client.event
async def on_message(message: discord.Message):
    num = message.author.id
    random.seed(num)
    num = random.randint(0, 4000)
    content = str(message.content)
    num = '$ ' + names[num] +': ' + content
    channel = client.get_channel(<channel ID>)
    if message.guild is None and not message.author.bot:
        await channel.send(num)

    await client.process_commands(message.author)

client.run("<token>")
