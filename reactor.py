import discord
import random
import os
import re
import asyncio
import requests as req

client = discord.Client()
async def daily():
    count = 0
    await client.wait_until_ready()
    while not client.is_closed:
        count += 1
        msg = str(count)
        await client.send_message(discord.Object(id='506143567400534016'), msg)
        await asyncio.sleep(3600)
'''async def alive():
    await client.wait_until_ready()
    while not client.is_closed:
        url = 'http://randompersonal.forum.wtf/'
        await asyncio.sleep(1800)
        keep = req.get(url)'''
    
@client.event
async def on_message(message):
     if message.author == client.user:
        return
     message.content = message.content.lower()
     if message.content.startswith('test'):
        msg = 'test alright'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.loop.create_task(daily())
client.run(os.getenv('TOKEN'))
