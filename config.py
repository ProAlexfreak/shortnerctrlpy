import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

DB_CHANNEL_ID = int(os.getenv("DB_CHANNEL_ID"))
DB_MESSAGE_ID = int(os.getenv("DB_MESSAGE_ID"))
