import os
from datetime import datetime
import requests
import discord


from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.content == "!ping":
            print("pong")
            await message.channel.send("pong")

        if message.content == "!time":
            current_datetime = datetime.now()
            print(current_datetime.strftime("%d.%m.%Y - %H:%M"))

            await message.channel.send(current_datetime.strftime("%d.%m.%Y - %H:%M"))

        if message.content[:8] == "!random ":
            obj = message.content[8:]
            resp = requests.get(f"https://some-random-api.ml/img/{obj}")

            if resp.status_code == 200:
                json_data = resp.json()
                embed = discord.Embed(
                    color=discord.Color.from_rgb(255, 0, 0), title=f"Random {obj}"
                )
                embed.set_image(url=json_data["link"])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(
                    """Упс, братишка твоего запроса нет😱
Попробуй что нибудь из этого:
    * `!random dog`
    * `!random cat`
    * `!random panda`
    * `!random red_panda`
    * `!random fox`
    * `!random birb`
    * `!random koala`
    * `!random kangaroo`
    * `!random racoon`
    * `!random whale`
    * `!random pikachu`
"""
                )

        print(f"Message from {message.author}: {message.content}")


client = MyClient()
client.run(TOKEN)
