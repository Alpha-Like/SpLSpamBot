from YashuAlpha.Database.sudo import is_sudo
from config import DEV

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID]

async def verify(id):
    if not await is_sudo(id):
        if not id in LEGENDS:
            return False
    return True
