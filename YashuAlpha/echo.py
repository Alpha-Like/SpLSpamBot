from config import DEV, STUFF

hl = STUFF.COMMAND_HANDLER

ECHO_USERS = []
async def echo(_, m):
    global RAID_IDS
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
    
