import discord
from discord.ext import tasks
import os
import asyncio
from datetime import datetime
import pytz

intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@tasks.loop(seconds = 3)
async def check_time():
    current_time_raw = datetime.now(pytz.timezone("America/Los_Angeles"))
    is_9 = (current_time_raw.strftime("%H") == "9") or (current_time_raw.strftime("%H") == "21")
    is_48 = current_time_raw.strftime("%M") == "48"
    is_948 = is_9 and is_48
    # Debug
    #is_hour = current_time_raw.strftime("%H") == "23"
    #is_minute = current_time_raw.strftime("%M") == "11"
    #is_time = is_hour and is_minute
    if is_948:
        general = client.get_channel(819377559753326625)
        await general.send("<@&1125671944335921282> wish!")
        await asyncio.sleep(60)
    #await check_time()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await check_time.start()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "car" in message.content.lower():
        await message.channel.send("Cyrussy <3")
    if "who are we" in message.content.lower():
        await message.channel.send("NRG! 9! 4! 8! YUH! ⚡")



client.run("u dont get my token ;)")