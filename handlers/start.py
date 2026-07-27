from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start"))
async def start_cmd(client, message):

    text = """
✨ **Welcome to Multi Shortener Bot**

🔗 Shorten URLs using multiple providers.

Select an option below.
"""

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔗 Short URL",
                    callback_data="short_menu"
                )
            ],
            [
                InlineKeyboardButton(
                    "⚙️ Admin Panel",
                    callback_data="admin_panel"
                )
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
