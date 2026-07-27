from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN

from handlers.start import register

app = Client(
    "MultiShortenerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register(app)

print("✅ Bot Started Successfully!")

app.run()
