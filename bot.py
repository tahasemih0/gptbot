
import discord
import openai

TOKEN = "BURAYA_DISCORD_BOT_TOKEN"
OPENAI_API_KEY = "BURAYA_OPENAI_API_KEY"

openai.api_key = OPENAI_API_KEY
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ai"):
        user_input = message.content[4:]
        await message.channel.typing()

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Sen bir yardımcı asistansın."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response["choices"][0]["message"]["content"]
            await message.channel.send(reply)

        except Exception as e:
            await message.channel.send(f"Hata: {e}")

client.run(TOKEN)
