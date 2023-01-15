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
        if await is_echo(m.from_user.id):
            if m.text:
                txt = m.text
                await m.reply(txt)
            elif m.sticker:
                id = m.sticker.file_id
                await m.reply_sticker(id)
            elif m.photo:
                id = m.photo.file_id
                caption = m.caption if m.caption else ""
                await m.reply_photo(id, caption=caption)
            elif m.video:
                id = m.video.file_id
                caption = m.caption if m.caption else ""
                await m.reply_video(id, caption=caption)
            elif m.animation:
                id = m.animation.file_id
                caption = m.caption if m.caption else ""
                await m.reply_animation(id, caption=caption)
            elif m.document:
                id = m.document.file_id
                caption = m.caption if m.caption else ""
                await m.reply_document(id, caption=caption)
            elif m.audio:
                id = m.audio.file_id
                caption = m.caption if m.caption else ""
                await m.reply_audio(id, caption=caption)
            elif m.voice:
                id = m.voice.file_id
                caption = m.caption if m.caption else ""
                await m.reply_voice(id, caption=caption)
            else:
                pass

async def echos(_, m):
    x = await get_echos()
    if not x:
        await m.reply("`No user is added to echo !`")
    txt = "**Echo Users :**\n\n"
    for y in x:
        txt += f"`{y}`\n"
    txt += "\n"
    txt += f"**Count : {len(x)}**"
    await m.reply(txt)
