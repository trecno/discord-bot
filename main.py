import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Estamos dentro como {0.user}'.format(client))

@client.event
async def on_message(message):
  author = message.author
  content = message.content
  channel = message.channel

  if author != client.user:
    if content.startswith('/hola'):
      await channel.send('¡Hola!')
    elif 'gracias' in content.lower():
      await channel.send('De nada', reference = message)
    else:
      await message.add_reaction('👍')

keep_alive()
client.run(os.environ['TOKEN'])
