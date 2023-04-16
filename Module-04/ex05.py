import discord
import os
import random

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

	if message.content.startswith("$help"):
		await all_commands(message)

	if message.content.startswith("$echo"):
		await message.channel.send(message.content[6:])

	if message.content.startswith("$say"):
		await message.channel.send(message.content[5:])
		await message.delete()

	if message.content.startswith("$rps"):
		await message.channel.send("Let's play rock, paper, scissors!")
	if message.content.startswith("$rock"):
		await play_rps(message, 'rock')
	elif message.content.startswith("$paper"):
		await play_rps(message, 'paper')
	elif message.content.startswith("$scissors"):
		await play_rps(message, 'scissors')

async def play_rps(message, p_move):
	rules = {
		"rock" : "scissors",
		"paper" : "rock",
		"scissors" : "paper"
	}

	bot_move = random.choice(list(rules))
	await message.channel.send(bot_move)

	if p_move == bot_move:
		await message.channel.send("It's a draw!")
	elif rules[p_move] == bot_move:
		await message.channel.send("You Win!")
	else:
		await message.channel.send("You Lose!")

	await message.channel.send(f"You chose {p_move}, the bot chose {bot_move}")

async def all_commands(message):
	await message.channel.send("""```
{:<10}- display all possible commands
{:<10}- make the bot repeat the users message
{:<10}- make the bot repeat messages, then delete the users message
{:<10}- play rock, paper, scissors with the user: [$rock, $paper, $scissors]
```""".format("$help", "$echo", "$say", "$rps")
	)

client.run(os.getenv("TOKEN"))