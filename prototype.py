import discord
import asyncio
import pyautogui
import time

client = discord.Client()

@client.event
async def on_ready():
		print('Logged in as', client.user.name, client.user.id)
		print('https://discordapp.com/oauth2/authorize?&client_id=379677652518174727&scope=bot+&permissions=8')

def keyboard(key):
		key = key.lower()

		if key in ['up', 'down', 'left', 'right']:
				pyautogui.press(key)
		else:
				pyautogui.typewrite(key[0])

@client.event
async def on_message(message):
		keyboard(message.content)
		
		#await client.send_message(message.channel, 'Typed it!')

import os
token = os.environ['token']
client.run(token)
