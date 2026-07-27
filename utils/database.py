from storage.telegram import load_database, save_database


async def get_shorteners(client):

    data = await load_database(client)

    return data["shorteners"]


async def update_shorteners(client, shorteners):

    data = await load_database(client)

    data["shorteners"] = shorteners

    await save_database(client, data)
