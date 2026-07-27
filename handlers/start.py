from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def register(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):

        text = f"""
✨ **Welcome to Multi Shortener Bot**

🔗 Shorten URLs using multiple providers.

📌 Features:
• Up to 10 Shorteners
• Stylish Interface
• Fast API Response

Choose an option below.
"""

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔗 Short URL", callback_data="short")
                ],
                [
                    InlineKeyboardButton("ℹ️ Help", callback_data="help")
                ]
            ]
        )

        await message.reply_text(
            text,
            reply_markup=buttons,
            disable_web_page_preview=True
        )
