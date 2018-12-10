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
        msg = message.content.format(message)
        idmsg = ('> ' + str(message.author) + ' | ' + str(message.author.id) + '''
''' + msg).format(message)
        await client.send_message(discord.Object(id='519415216547823616'), msg)
        await client.send_message(discord.Object(id='521658881710227457'), idmsg)
     message.content = message.content.lower()
     if message.channel.id == '519415216547823616':
        if message.content.startswith('!пидорпомоги'):
            msg = ('''Хуе-мое, смотри сюда значит, есть такие команды:
!пидор
!главпидор
!ктоя
!кока
!вождь
!сплит
Если ты весь такой из себя дохуя аноним, то пиши мне в личку, я передам питухам.''').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!главпидор'):
            msg = ('<@323030642419826689> - главный пидор нашего сообщества, горжусь им.').format(message) 
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!кока'):
            await client.send_file(discord.Object(id='519415216547823616'), './koka.png')
        elif message.content.startswith('!вождь'):
            await client.send_file(discord.Object(id='519415216547823616'), './rel.png')
        elif message.content.startswith('!сплит'):
            await client.send_file(discord.Object(id='519415216547823616'), './split.png')
        elif message.author == client.user:
            return
        elif message.content.startswith('!ктоя'):
            if (int(message.author.id) % 2 == 0): msg = ('<@' + str(message.author.id) + '>, ты рилкобот').format(message)
            elif message.author.id == '435413273500844033': msg = ('<@' + str(message.author.id) + '>, ты и есть Мишванда').format(message)
            else: msg = ('<@' + str(message.author.id) + '>, ты твинк Мишванды').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!пидор'):
            msg = ('<@' + str(message.author.id) + '>, ты пидор').format(message) 
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!'):
            msg = 'Чтобы посмотреть список текущих комманд, хуяни !пидорпомоги'.format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
#client.loop.create_task(daily())
client.run(os.getenv('TOKEN'))
