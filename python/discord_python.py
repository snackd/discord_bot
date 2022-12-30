import os
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 使用client class
client = client = discord.Client(intents=discord.Intents.default())


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

    if message.content.startswith('你好'):
        await message.channel.send('你好呀OuO')

client.run(TOKEN)
