import discord
import random
import os
import re
import asyncio

client = discord.Client()
'''async def daily():
    await client.wait_until_ready()
    while not client.is_closed:
        await asyncio.sleep(86400)
        await client.send_message(discord.Object(id='517088248053628929'), 'Новости дня: Кока - пидор.')'''

@client.event
async def on_message(message):
     if message.author == client.user:
            return
     '''if message.content.startswith('!бросок'):
            nums = re.findall('\d+', message.content)
            nums = list(map(int, nums))
            if len(nums) > 2 or nums[0] > 100 or nums[0] == 0 or nums[1] == 0 or nums[1] > 100:
                msg = 'иди нахуй'
            else:
                res = 0
                dice = []
                for x in range(nums[0]):
                    die = random.randint(1, nums[1])
                    dice.append(die)
                    res += die
                msg = 'Итого: ' + str(res).format(message)
                await client.send_message(message.channel, dice)
            await client.send_message(message.channel, msg)'''
     if message.channel in client.private_channels:
        msg = message.content
        await client.send_message(discord.Object(id='519415216547823616'), msg)
     message.content = message.content.lower()
     if message.channel.id == '519415216547823616':
        if message.content.startswith('!бан'):
            user = message.author.id
            msg = ('<@' + str(user) + '>, ты рилкобот').format(message) 
            await client.send_message(message.channel, msg)
        elif message.content.startswith('!пидор'):
            user = message.author.id
            msg = ('<@' + str(user) + '>, ты пидор').format(message) 
            await client.send_message(message.channel, msg)
        elif message.content.startswith('!мишванда'):
            msg = 'Хуй тебе, а не Мишванда'.format(message)
            await client.send_message(message.channel, msg)
        elif message.content.startswith('!хомяк'):
            await client.send_message(message.channel, 'Хомяки!')
        elif message.content.startswith('!кока'):
            await client.send_file(message.channel, './koka.png')
        elif message.content.startswith('!вождь'):
            await client.send_file(message.channel, './rel.png')
        elif message.content.startswith('!сплит'):
            await client.send_file(message.channel, './split.png')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
#client.loop.create_task(daily())
client.run(os.getenv('TOKEN'))
