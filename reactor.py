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
     tmpsg = message.content
     if message.channel in client.private_channels:
        if message.content.startswith('!цветной'):
            womsg = tmpsg[9:]
            lang = ('diff', 'CSS', 'yaml', 'fix', 'brainfuck')               
            colr = random.choice(lang)
            if colr == 'diff': mns = '-'
            else: mns = ''
            msg = ('''```''' + colr + '''
''' + mns + womsg + '''
```''').format(message)
        else:
            msg = message.content.format(message)
        idmsg = ('> ' + str(message.author) + ' | ' + str(message.author.id) + '''
''' + msg).format(message)
        await client.send_message(discord.Object(id='519415216547823616'), msg)
        await client.send_message(discord.Object(id='521658881710227457'), idmsg)
     
     message.content = message.content.lower()
     if message.channel.id == '519415216547823616':
        if message.content.startswith('!пидорпомоги'):
            msg = ('''Хуе-мое, смотри сюда значит, есть такие команды:
!цветной (текст; только лс)
!пидор
!главпидор
!ктоя
!ктоты (линк на юзера)
!кока
!вождь
!сплит
Если ты весь такой из себя дохуя аноним, то пиши мне в личку, я передам питухам.''').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!главпидор'):
            msg = ('<@517401689532137484> - главный пидор нашего сообщества, он соснет тебе.').format(message) 
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!кока'):
            await client.send_file(discord.Object(id='519415216547823616'), './koka.png')
        elif message.content.startswith('!вождь'):
            await client.send_file(discord.Object(id='519415216547823616'), './rel.png')
        elif message.content.startswith('!сплит'):
            await client.send_file(discord.Object(id='519415216547823616'), './split.png')
        elif message.content.startswith('!пидор'):
            if len(message.mentions) > 0 and message.mentions[0].id is not '517242247771586574':
                msg = ('<@' + str(message.mentions[0].id) + '>, ты пидор').format(message)
            else:                   
                msg = ('<@' + str(message.author.id) + '>, ты пидор').format(message)
                if message.channel in client.private_channels:
                    await client.send_message(message.author, msg)
                    return
            await client.send_message(discord.Object(id='519415216547823616'), msg)
        elif message.content.startswith('!ктоты'):
            if (int(message.mentions[0].id) % 2 == 0): msg = ('<@' + str(message.mentions[0].id) + '> - рилкобот').format(message)
            elif message.mentions[0].id == '435413273500844033': msg = ('<@' + str(message.mentions[0].id) + '> - сама Мишванда').format(message)
            elif message.mentions[0].id == '517242247771586574': msg = ('<@' + str(message.mentions[0].id) + '> - Анон, ты что, тупой?').format(message)  
            elif message.mentions[0].id == '314363965125820417': msg = ('<@' + str(message.mentions[0].id) + '> - шоколадное очко').format(message)    
            else: msg = ('<@' + str(message.mentions[0]) + '> - твинк Мишванды').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
           
        elif message.author == client.user:
            return
        elif message.content.startswith('!ктоя'):
            if (int(message.author.id) % 2 == 0): msg = ('<@' + str(message.author.id) + '>, ты рилкобот').format(message)
            elif message.author.id == '435413273500844033': msg = ('<@' + str(message.author.id) + '>, ты и есть Мишванда').format(message)
            elif message.author.id == '314363965125820417': msg = ('<@' + str(message.author.id) + '>, ты шоколадное очко').format(message)
            else: msg = ('<@' + str(message.author.id) + '>, ты твинк Мишванды').format(message)
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
