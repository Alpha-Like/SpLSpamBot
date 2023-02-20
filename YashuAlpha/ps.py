from .verify import verify
from .data import PORMS
import random
from config import STUFF

hl = STUFF.COMMAND_HANDLER

async def ps(_, m):
  if not await verify(m.from_user.id):
    return
  if not STUFF.ALLOW_PORN:
    return await m.reply("Porn spam is disabled ! For enabling, set ALLOW_PORN to True in config !")
  try:
    count = int(m.text.split()[1])
  except:
    return await m.reply(f"{hl}pornspam | {hl}ps [count]")
  for i in range(0, count):
    med = random.choice(PORMS)
    if med[-3:] == "mp4":
        await _.send_animation(m.chat.id, med)
    else:
        await _.send_photo(m.chat.id, med)

