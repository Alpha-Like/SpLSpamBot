from config import DEV, STUFF
from .data import KeshavX
from YashuAlpha.Database.echo import *

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

async def addecho(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}addecho [username|id|reply]`")
    if id in LEGENDS:
        return await m.reply("`CAN'T ECHO THEM !`")
    if await is_echo(id):
        return await m.reply("`ECHO IS ALREADY ACTIVATED TO THIS USER !`")
    await add_echo(id)
    await m.reply(f"`ECHO ACTIVATED TO THE USER `<code>{id}</code>")

async def rmecho(_, m):
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"`{hl}addecho [username|id|reply]`")
    
    if not await is_echo(id):
        return await m.reply("`USER NOT IN ECHO LIST !`")
    await del_echo(id)
    await m.reply(f"`ECHO DEACTIVATED TO THE USER `<code>{id}</code>")

async def echo_cwf(_, m):
    if m.from_user:
        if m.from_user.id in ECHO_USERS:
            if m.text:
                txt = m.text
                await m.reply(txt)
            elif m.sticker:
                id = m.sticker.file_id
                await m.reply_sticker(id)
            elif m.photo:
                x = await _.download_media(m)
                await m.reply_photo(x)
            else:
                pass
