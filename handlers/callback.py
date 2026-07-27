from pyrogram import Client
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


@Client.on_callback_query()
async def callback_handler(client, query: CallbackQuery):

    data = query.data

    if data == "short_menu":

        await query.message.edit_text(
            "🔗 **Choose a Shortener**\n\n"
            "No shorteners have been added yet.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "◀ Back",
                            callback_data="home"
                        )
                    ]
                ]
            )
        )

    elif data == "admin_panel":

        await query.message.edit_text(
            "⚙️ **Admin Panel**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Add Shortener",
                            callback_data="add_shortener"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "📝 Edit Shortener",
                            callback_data="edit_shortener"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "🗑 Delete Shortener",
                            callback_data="delete_shortener"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "◀ Back",
                            callback_data="home"
                        )
                    ]
                ]
            )
        )

    elif data == "home":

        await query.message.edit_text(
            "✨ **Welcome to Multi Shortener Bot**",
            reply_markup=InlineKeyboardMarkup(
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
        )

    await query.answer()
