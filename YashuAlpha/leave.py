from config import DEV
from .data import KeshavX
from .verify import verify

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

async def leave(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id = int(m.text.split()[1])
    except:
        id = m.chat.id
    await m.reply("LEFT CHAT ✅ ")
    await _.leave_chat(id)
    
