from .raid import KeshavX, GROUP

async def spam(_, m):
    if m.chat.id in GROUP:
        return await m.reply("CAN'T SPAM IN OWNER's GROUP ! 🌝✨")
