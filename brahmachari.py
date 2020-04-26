import discord
import random
import string
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    
    bad_words = [] #list bad words you want to restrict.

    msg_list = [] # list message you want to send to user in the channel.
    
    table = str.maketrans(dict.fromkeys(string.punctuation))
    content = message.content.translate(table)    
    content = content.replace(" ","")
    content = content.lower()
    
    for word in bad_words:
        
        if word in content:
            await message.channel.purge(limit=1)
            usr = str(message.author)
            usr = usr[:usr.index('#')]
            msgs = []
            msg = await message.channel.send(usr + random.choice(msg_list) + " \n No gaali coz i'm brahmachari. \n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            msgs.append(msg)
            await asyncio.sleep(3)
            await message.channel.delete_messages(msgs)
            
client.run("your-token-here")

