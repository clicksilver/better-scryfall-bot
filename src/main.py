import interactions
import token

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start(token.bot_token)
