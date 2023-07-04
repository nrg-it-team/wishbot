# This repository will likely not be updated.
# Please refer to https://replit.com/@cjplusplus/wishbot.

import discord
from discord.ext import tasks
import os
import asyncio
from datetime import datetime
import pytz
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@tasks.loop(seconds=3)
async def check_time():
  current_time_raw = datetime.now(pytz.timezone("America/Los_Angeles"))
  is_9 = (current_time_raw.strftime("%H")
          == "9") or (current_time_raw.strftime("%H") == "21")
  is_48 = current_time_raw.strftime("%M") == "48"
  is_948 = is_9 and is_48
  # Debug
  #is_hour = current_time_raw.strftime("%H") == "23"
  #is_minute = current_time_raw.strftime("%M") == "11"
  #is_time = is_hour and is_minute
  if is_948:
    general = client.get_channel(921915887521509418)
    await general.send("<@&1125686347076751433> wish!")
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
    await message.channel.send("<@949464689249775656> <3")
  if "who are we" in message.content.lower():
    await message.channel.send("NRG! 9! 4! 8! YUH! ⚡")
  if os.getenv("KILLSWITCH") in message.content.lower():
    await message.channel.send(
      "Emergency shutdown protocol initiated. Please contact <@497586303387566106> if you see this message."
    )
    await client.close()


keep_alive()
client.run(os.getenv("TOKEN"))
