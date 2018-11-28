import discord
import random
import os
import re
import asyncio
#from apscheduler.schedulers.blocking import BlockingScheduler

#sched = BlockingScheduler()
client = discord.Client()

'''@sched.scheduled_job('interval', minutes=3)
async def timed_job():
    await client.send_message(discord.Object(id='506143567400534016'), 'This job is run every three minutes.')'''

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
#sched.start()
client.run(os.getenv('TOKEN'))
