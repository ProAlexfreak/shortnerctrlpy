from pyrogram.errors import RPCError
from config import DB_CHANNEL_ID


async def save_data(client, text):
    """
    Save data as a new message in the DB channel.
    Returns the message ID.
    """
    try:
        msg = await client.send_message(
            chat_id=DB_CHANNEL_ID,
            text=text,
            disable_web_page_preview=True
        )
        return msg.id
    except RPCError as e:
        print(f"Database Error: {e}")
        return None


async def edit_data(client, message_id, text):
    """
    Edit an existing database message.
    """
    try:
        await client.edit_message_text(
            chat_id=DB_CHANNEL_ID,
            message_id=message_id,
            text=text,
            disable_web_page_preview=True
        )
        return True
    except RPCError as e:
        print(f"Database Error: {e}")
        return False


async def read_data(client, message_id):
    """
    Read one database message.
    """
    try:
        msg = await client.get_messages(
            DB_CHANNEL_ID,
            message_id
        )
        return msg.text
    except RPCError as e:
        print(f"Database Error: {e}")
        return None


async def delete_data(client, message_id):
    """
    Delete a database message.
    """
    try:
        await client.delete_messages(
            DB_CHANNEL_ID,
            message_id
        )
        return True
    except RPCError as e:
        print(f"Database Error: {e}")
        return False
