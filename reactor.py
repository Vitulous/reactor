import discord
import random
import os
import re
import asyncio
import cv2
from googletrans import Translator
from moviepy.editor import *
#import youtube_dl

translator = Translator()
langs = ("af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu", "fil", "he")

#ydl = youtube_dl.YoutubeDL({'outtmpl': 'ytvid.mp4',
#                            'format': '135'})



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
!миша
!охлади (текст)
!? (вопрос)
Если ты весь такой из себя дохуя аноним, то пиши мне в личку, я передам питухам.''').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
            
        elif message.content.startswith('!главпидор'):
            msg = ('<@516251605864153099> - главный пидор нашего сообщества, хочет он этого, или нет.').format(message) 
            await client.send_message(discord.Object(id='519415216547823616'), msg)
            
        elif message.content.startswith('!кока'):
            await client.send_file(discord.Object(id='519415216547823616'), './koka.png')
            
        elif message.content.startswith('!вождь'):
            await client.send_file(discord.Object(id='519415216547823616'), './rel.png')
            
        elif message.content.startswith('!сплит'):
            await client.send_file(discord.Object(id='519415216547823616'), './split.png')
            
        elif message.content.startswith('!миш'):
            await client.send_file(discord.Object(id='519415216547823616'), './mishvanda.png')
            
        elif message.content.startswith('!охлади'):
            uwu = tmpsg[8:]
            for i in range (10):
                owo = random.choice(langs)
                ttext = translator.translate(uwu, dest=owo).text
                uwu = ttext
            ttext = translator.translate(uwu, dest='ru').text
            msg = ttext.format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
            
        elif message.content.startswith('!?'):
            ebanswer = ('Полюбому', 'Точно', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Есть все шансы', 'Да? Наверное?', 'Да', 'Хуй его знает', 'Иди нахуй с такими вопросами', 'Не скажу', 'Спроси у бати', 'Хули ты мне такие вопросы задаешь?', 'И не надейся', 'Хуй там', 'Нет', 'Не лезь туда, дибил', 'Весьма сомнительно')
            msg = random.choice(ebanswer).format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
            
        elif message.content.startswith('!пидор'):
            if len(message.mentions) > 0 and message.mentions[0].id is not '517242247771586574':
                msg = ('<@' + str(message.mentions[0].id) + '>, ты пидор').format(message)
            elif message.author.id == '517242247771586574':
                return
            else:                   
                msg = ('<@' + str(message.author.id) + '>, ты пидор').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
            
        elif message.content.startswith('!ктоты'):
            if (int(message.mentions[0].id) % 2 == 0): msg = ('<@' + str(message.mentions[0].id) + '> - рилкобот').format(message)
            elif message.mentions[0].id == '435413273500844033': msg = ('<@' + str(message.mentions[0].id) + '> - сама Мишванда').format(message)
            elif message.mentions[0].id == '516251605864153099': msg = ('<@' + str(message.mentions[0].id) + '> - пидор').format(message) 
            elif message.mentions[0].id == '279345329139351563': msg = ('<@' + str(message.mentions[0].id) + '> - лох, что вечно промазывает').format(message)
            elif message.mentions[0].id == '517058500896096257': msg = ('<@' + str(message.mentions[0].id) + '> - натурал').format(message)  
            elif message.mentions[0].id == '314363965125820417': msg = ('<@' + str(message.mentions[0].id) + '> - шоколадное очко').format(message)    
            else: msg = ('<@' + str(message.mentions[0].id) + '> - твинк Мишванды').format(message)
            await client.send_message(discord.Object(id='519415216547823616'), msg)
           
        elif message.author == client.user:
            return
        
        elif message.content.startswith('!ктоя'):
            if (int(message.author.id) % 2 == 0): msg = ('<@' + str(message.author.id) + '>, ты рилкобот').format(message)
            elif message.author.id == '435413273500844033': msg = ('<@' + str(message.author.id) + '>, ты и есть Мишванда').format(message)
            elif message.author.id == '314363965125820417': msg = ('<@' + str(message.author.id) + '>, ты шоколадное очко').format(message)
            elif message.author.id == '516251605864153099': msg = ('<@' + str(message.author.id) + '>, ты пидор').format(message)  
            elif message.author.id == '517058500896096257': msg = ('<@' + str(message.author.id) + '>, ты натурал').format(message)  
            elif message.author.id == '279345329139351563': msg = ('<@' + str(message.author.id) + '>, ты лох, что вечно промазывает').format(message)
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
