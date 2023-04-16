import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')
    
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("$say"):
		await message.channel.send(message.content[5:])
		await message.delete()
		
client.run(os.getenv("TOKEN"))