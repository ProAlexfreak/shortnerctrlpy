import json

from config import DB_CHANNEL_ID, DB_MESSAGE_ID


async def load_database(client):
    msg = await client.get_messages(
        DB_CHANNEL_ID,
        DB_MESSAGE_ID
    )

    return json.loads(msg.text)


async def save_database(client, data):

    await client.edit_message_text(
        DB_CHANNEL_ID,
        DB_MESSAGE_ID,
        json.dumps(
            data,
            indent=4
        )
    )
