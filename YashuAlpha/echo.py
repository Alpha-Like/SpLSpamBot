from config import DEV, STUFF

hl = STUFF.COMMAND_HANDLER

ECHO_USERS = []
async def echo(_, m):
    global ECHO_USERS
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
        return await m.reply(f"{hl}addecho [username|id|reply]")
    if id in (DEV.SUDO_USERS) or id == DEV.OWNER_ID:
        return await m.reply("CAN'T ECHO THEM !")
    if id in ECHO_USERS:
        return await m.reply("ECHO IS ALREADY ACTIVATED TO THIS USER !")
    ECHO_USERS.append(id)
    await m.reply("ECHO ACTIVATED TO THE USER" + <code>str(id)</code>)

async def echo(_, m):
    global ECHO_USERS
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
        return await m.reply(f"{hl}addecho [username|id|reply]")
    
    if not id in ECHO_USERS:
        return await m.reply("USER NOT IN ECHO LIST !")
    ECHO_USERS.remove(id)
    await m.reply("ECHO DEACTIVATED TO THE USER" + <code>str(id)</code>)

async def echo_cwf(_, m):
    if m.from_user:
        if m.from_user.id in ECHO_USERS:
            if m.text:
                txt = m.text
                await m.reply(txt)
            elif m.sticker:
                id = m.sticker.id
                await m.reply_sticker(id)
            elif m.photo:
                x = await _.download_media(m)
                await m.reply_photo(x)
            else:
                pass
