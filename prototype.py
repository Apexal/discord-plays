import discord
import asyncio
import pyautogui
import os

client = discord.Client()

control_channel_id = '222576355362078731'
owner_user_id = '152621041976344577' # My Discord ID

class Player:
    def __init__(self):
        self.listening = True

    def handle_input(self, input, is_owner=False):
        if input == 'stop listening' and is_owner:
            self.listening = False
            print('Stopped listening...')
        elif input == 'start listening' and is_owner:
            self.listening = True
            print('Started listening...')
        elif self.listening:
            for text in input.split(' '):
                text = text.lower()

                self.keyboard(text)
                print(text)

    def keyboard(self, key):
        key = key.lower()

        if key in ['up', 'down', 'left', 'right', 'enter', 'return', 'shift', 'escape']:
            pyautogui.press(key)
        else:
            pyautogui.typewrite(key, interval=0.2)

@client.event
async def on_error(event):
    raise

@client.event
async def on_message(message):
    if not message.author.bot:
        player.handle_input(message.content, message.author.id == owner_user_id)

@client.event
async def on_ready():
    print('Logged in as', client.user.name, client.user.id)
    print('https://discordapp.com/oauth2/authorize?&client_id=379677652518174727&scope=bot+&permissions=8')

player = Player()
token = os.environ['token']
client.run(token)
