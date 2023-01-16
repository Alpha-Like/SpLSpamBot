import time
from . import startTime
from config import STUFF, DEV
from .verify import verify

OWNER = DEV.OWNER_ID

hl = STUFF.COMMAND_HANDLER

TEXT = """

💞Pong💞

   🔸️ {}
   🔹️ 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛 ~ {}

"""

def grt(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

async def ping(_, m):
    if not await verify(m.from_user.id)
        return
    st = time.time()
    ok = await eor(m, "`Checking...`")
    end = time.time()
    men = (await _.get_users(OWNER)).mention
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [𝚂𝙿𝙻](t.me/SpLBots)\n"
    return await ok.edit(TEXT.format(pong, men))
