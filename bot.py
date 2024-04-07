# This repository will likely not be updated.
# Please refer to https://replit.com/@cjplusplus/wishbot.

import slack
import os
import asyncio
from datetime import datetime
import pytz
from pathlib import Path
from dotenv import load_dotenv
from keep_alive import keep_alive

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
client.chat_postMessage(channel="#wish", text="Wishbot is online!")


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
    client.chat_postMessage(channel="#wish", text="<!channel> 9:48! Make a wish! ✨⚡")
    return True
  return False


async def main_loop(interval=2):
  while True:
    if await check_time():
      await asyncio.sleep(60) # Pauses bot for a minute to eliminate duplicate wishes
    else:
      await asyncio.sleep(interval)
keep_alive()
asyncio.run(main_loop())
"""
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
client.run(os.getenv("TOKEN"))"""
