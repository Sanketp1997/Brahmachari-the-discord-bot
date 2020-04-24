import discord
import random
import string
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    
    bad_words = ["bc", "mc", "chutiya", "lund","gand","chu","asshole","chodu","lodu","randi","loda","bhangi","fuck","fcuk","fuk","aukat"
    ,"laude","lavde","bhangi","madarc","bhen","wtf","pikina","tf","maa ki","bsdk","rndi","gandu","mader","suck","bitch"]

    msg_list = [" your message was deleted"," you are disguisting."," saale gaali kisko bola?", " sorry we don't speak that here. :)"," gaado nai bolvani. #peace"," yeh koi r@#dikha#a hai?",
    " Gaandu salaa!"," <-- Ashleel hai yeh launda"]
    
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

