from .data import RAID, REPLYRAID
import random
from config import STUFF
import asyncio

hl = STUFF.COMMAND_HANDLER

async def raid(_, m):
    try:
        count = int(m.text.split()[1])
    except:
        return await m.reply(f"{hl}raid [count]")
    for c in range(0, count):
        raid = random.choice(RAID)
        if m.reply_to_message:
            await m.reply_to_message.reply(raid)
        else:
            await _.send_message(m.chat.id, raid)
        await asyncio.sleep(0.02)

RAID_IDS = []
async def replyraid(_, m):
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
        return await m.reply(f"{hl}replyraid [id|username|reply]")
    
    RAID_IDS.append(id)
    return await m.reply("RAID REPLY ACTIVATED TO USER" + str(id))

    
    
