import interactions
import tokens 

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start(tokens.BOT_TOKEN)
