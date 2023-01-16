from pyrogram import Client, filters, idle
from config import *
import time
from YashuAlpha.plugins import start, help, cmds_cbq, close_cbq, raid_cbq, extra_cbq, spam_cbq
from YashuAlpha.raid import raid, replyraid, dreplyraid, raid_cwf
from YashuAlpha.data import KeshavX
from YashuAlpha.spam import spam_func, dspam_func
from YashuAlpha.echo import addecho, rmecho, echo_cwf, echos
from YashuAlpha.leave import leave
from YashuAlpha.sudo import add_or_del_sudo, sudo_users
from YashuAlpha.alive_ping import ping, aliver 

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

LEGEND = DEV.OWNER_ID

END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)
END2 = Client(":END2:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_2)
END3 = Client(":END3:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_3)
END4 = Client(":END4:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_4)
END5 = Client(":END5:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_5)
END6 = Client(":END6:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_6)
END7 = Client(":END7:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_7)
END8 = Client(":END8:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_8)
END9 = Client(":END9:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_9)
END10 = Client(":END10:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_10)

@END.on_message(filters.command("help", hl))
@END2.on_message(filters.command("help", hl))
@END3.on_message(filters.command("help", hl))
@END4.on_message(filters.command("help", hl))
@END5.on_message(filters.command("help", hl))
@END6.on_message(filters.command("help", hl))
@END7.on_message(filters.command("help", hl))
@END8.on_message(filters.command("help", hl))
@END9.on_message(filters.command("help", hl))
@END10.on_message(filters.command("help", hl))
async def help_plug(_, m):
    await help(_, m)

print("[module] loaded :- help")

@END.on_message(filters.command("ping", hl))
@END2.on_message(filters.command("ping", hl))
@END3.on_message(filters.command("ping", hl))
@END4.on_message(filters.command("ping", hl))
@END5.on_message(filters.command("ping", hl))
@END6.on_message(filters.command("ping", hl))
@END7.on_message(filters.command("ping", hl))
@END8.on_message(filters.command("ping", hl))
@END9.on_message(filters.command("ping", hl))
@END10.on_message(filters.command("ping", hl))
async def ping_plug(_, m):
    await ping(_, m)

print("\n[module] loaded :- ping")

@END.on_message(filters.command("alive", hl))
@END2.on_message(filters.command("alive", hl))
@END3.on_message(filters.command("alive", hl))
@END4.on_message(filters.command("alive", hl))
@END5.on_message(filters.command("alive", hl))
@END6.on_message(filters.command("alive", hl))
@END7.on_message(filters.command("alive", hl))
@END8.on_message(filters.command("alive", hl))
@END9.on_message(filters.command("alive", hl))
@END10.on_message(filters.command("alive", hl))
async def alive_plug(_, m):
    await aliver(_, m)

print("[module] loaded :- alive")

@END.on_message(filters.command("spam", hl))
@END2.on_message(filters.command("spam", hl))
@END3.on_message(filters.command("spam", hl))
@END4.on_message(filters.command("spam", hl))
@END5.on_message(filters.command("spam", hl))
@END6.on_message(filters.command("spam", hl))
@END7.on_message(filters.command("spam", hl))
@END8.on_message(filters.command("spam", hl))
@END9.on_message(filters.command("spam", hl))
@END10.on_message(filters.command("spam", hl))
async def spam_plug(_, m):
    await spam_func(_, m)

print("\n[module] loaded :- spam")

@END.on_message(filters.command("dspam", hl))
@END2.on_message(filters.command("dspam", hl))
@END3.on_message(filters.command("dspam", hl))
@END4.on_message(filters.command("dspam", hl))
@END5.on_message(filters.command("dspam", hl))
@END6.on_message(filters.command("dspam", hl))
@END7.on_message(filters.command("dspam", hl))
@END8.on_message(filters.command("dspam", hl))
@END9.on_message(filters.command("dspam", hl))
@END10.on_message(filters.command("dspam", hl))
async def dspam_plug(_, m):
    await dspam_func(_, m)

print("\n[module] loaded :- dspam")

@END.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END2.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END3.on_message(filters.command(["addsudo", "rmsudo"], hl)& filters.user(LEGEND))
@END4.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END5.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END6.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END7.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END8.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END9.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
@END10.on_message(filters.command(["addsudo", "rmsudo"], hl) & filters.user(LEGEND))
async def sudo_plug(_, m):
    await add_or_del_sudo(_, m)

@END.on_message(filters.command("sudos", hl))
@END2.on_message(filters.command("sudos", hl))
@END3.on_message(filters.command("sudos", hl))
@END4.on_message(filters.command("sudos", hl))
@END5.on_message(filters.command("sudos", hl))
@END6.on_message(filters.command("sudos", hl))
@END7.on_message(filters.command("sudos", hl))
@END8.on_message(filters.command("sudos", hl))
@END9.on_message(filters.command("sudos", hl))
@END10.on_message(filters.command("sudos", hl))
async def gsudo_plug(_, m):
    await sudo_users(_, m)

print("\n[module] loaded :- sudos")

@END.on_message(filters.command("addecho", hl))
@END2.on_message(filters.command("addecho", hl))
@END3.on_message(filters.command("addecho", hl))
@END4.on_message(filters.command("addecho", hl))
@END5.on_message(filters.command("addecho", hl))
@END6.on_message(filters.command("addecho", hl))
@END7.on_message(filters.command("addecho", hl))
@END8.on_message(filters.command("addecho", hl))
@END9.on_message(filters.command("addecho", hl))
@END10.on_message(filters.command("addecho", hl))
async def addecho_plug(_, m):
    await addecho(_, m)

print("\n[module] loaded :- addecho")

@END.on_message(filters.command("rmecho", hl))
@END2.on_message(filters.command("rmecho", hl))
@END3.on_message(filters.command("rmecho", hl))
@END4.on_message(filters.command("rmecho", hl))
@END5.on_message(filters.command("rmecho", hl))
@END6.on_message(filters.command("rmecho", hl))
@END7.on_message(filters.command("rmecho", hl))
@END8.on_message(filters.command("rmecho", hl))
@END9.on_message(filters.command("rmecho", hl))
@END10.on_message(filters.command("rmecho", hl))
async def rmecho_plug(_, m):
    await rmecho(_, m)

print("\n[module] loaded :- rmecho")

@END.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("echos", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("echos", hl) & filters.user(LEGENDS))
async def echos_plug(_, m):
    await echos(_, m)

@END.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("raid", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("raid", hl) & filters.user(LEGENDS))
async def raid_plug(_, m):
    await raid(_, m)

print("\n[module] loaded :- raid")

@END.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("replyraid", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("replyraid", hl) & filters.user(LEGENDS))
async def replyraid_plug(_, m):
    await replyraid(_, m)

print("\n[module] loaded :- replyraid")

@END.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("dreplyraid", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("dreplyraid", hl) & filters.user(LEGENDS))
async def dreplyraid_plug(_, m):
    await dreplyraid(_, m)

print("\n[module] loaded :- dreplyraid")

@END.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("leave", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("leave", hl) & filters.user(LEGENDS))
async def leave_plug(_, m):
    await leave(_, m)

print("\n[module] loaded :- leave")

@END.on_message(filters.command("start", [hl, "/"]))
@END2.on_message(filters.command("start", [hl, "/"]))
@END3.on_message(filters.command("start", [hl, "/"]))
@END4.on_message(filters.command("start", [hl, "/"]))
@END5.on_message(filters.command("start", [hl, "/"]))
@END6.on_message(filters.command("start", [hl, "/"]))
@END7.on_message(filters.command("start", [hl, "/"]))
@END8.on_message(filters.command("start", [hl, "/"]))
@END9.on_message(filters.command("start", [hl, "/"]))
@END10.on_message(filters.command("start", [hl, "/"]))
async def start_plug(_, m):
    await start(_, m)

print("\n[module] loaded :- start")

@END.on_callback_query(filters.regex("cmds"))
@END2.on_callback_query(filters.regex("cmds"))
@END3.on_callback_query(filters.regex("cmds"))
@END4.on_callback_query(filters.regex("cmds"))
@END5.on_callback_query(filters.regex("cmds"))
@END6.on_callback_query(filters.regex("cmds"))
@END7.on_callback_query(filters.regex("cmds"))
@END8.on_callback_query(filters.regex("cmds"))
@END9.on_callback_query(filters.regex("cmds"))
@END10.on_callback_query(filters.regex("cmds"))
async def cmds_cbq_plug(_, q):
    await cmds_cbq(_, q)

print("\n[module] loaded :- cmds_cbq")

@END.on_callback_query(filters.regex("spam"))
@END2.on_callback_query(filters.regex("spam"))
@END3.on_callback_query(filters.regex("spam"))
@END4.on_callback_query(filters.regex("spam"))
@END5.on_callback_query(filters.regex("spam"))
@END6.on_callback_query(filters.regex("spam"))
@END7.on_callback_query(filters.regex("spam"))
@END8.on_callback_query(filters.regex("spam"))
@END9.on_callback_query(filters.regex("spam"))
@END10.on_callback_query(filters.regex("spam"))
async def spam_cbq_plug(_, q):
    await spam_cbq(_, q)

print("\n[module] loaded :- spam_cbq")

@END.on_callback_query(filters.regex("raid"))
@END2.on_callback_query(filters.regex("raid"))
@END3.on_callback_query(filters.regex("raid"))
@END4.on_callback_query(filters.regex("raid"))
@END5.on_callback_query(filters.regex("raid"))
@END6.on_callback_query(filters.regex("raid"))
@END7.on_callback_query(filters.regex("raid"))
@END8.on_callback_query(filters.regex("raid"))
@END9.on_callback_query(filters.regex("raid"))
@END10.on_callback_query(filters.regex("raid"))
async def raid_cbq_plug(_, q):
    await raid_cbq(_, q)

print("\n[module] loaded :- raid_cbq")

@END.on_callback_query(filters.regex("extra"))
@END2.on_callback_query(filters.regex("extra"))
@END3.on_callback_query(filters.regex("extra"))
@END4.on_callback_query(filters.regex("extra"))
@END5.on_callback_query(filters.regex("extra"))
@END6.on_callback_query(filters.regex("extra"))
@END7.on_callback_query(filters.regex("extra"))
@END8.on_callback_query(filters.regex("extra"))
@END9.on_callback_query(filters.regex("extra"))
@END10.on_callback_query(filters.regex("extra"))
async def extra_cbq_plug(_, q):
    await extra_cbq(_, q)

print("\n[module] loaded :- extra_cbq")

@END.on_callback_query(filters.regex("close"))
@END2.on_callback_query(filters.regex("close"))
@END3.on_callback_query(filters.regex("close"))
@END4.on_callback_query(filters.regex("close"))
@END5.on_callback_query(filters.regex("close"))
@END6.on_callback_query(filters.regex("close"))
@END7.on_callback_query(filters.regex("close"))
@END8.on_callback_query(filters.regex("close"))
@END9.on_callback_query(filters.regex("close"))
@END10.on_callback_query(filters.regex("close"))
async def close_cbq_plug(_, q):
    await close_cbq(_, q)

print("\n[module] loaded :- close_cbq")

@END.on_message(group=1)
@END2.on_message(group=1)
@END3.on_message(group=1)
@END4.on_message(group=1)
@END5.on_message(group=1)
@END6.on_message(group=1)
@END7.on_message(group=1)
@END8.on_message(group=1)
@END9.on_message(group=1)
@END10.on_message(group=1)
async def echo_cwf_plug(_, m):
    await echo_cwf(_, m)

print("\n[module] loaded :- echo_cwf")

@END.on_message(group=2)
@END2.on_message(group=2)
@END3.on_message(group=2)
@END4.on_message(group=2)
@END5.on_message(group=2)
@END6.on_message(group=2)
@END7.on_message(group=2)
@END8.on_message(group=2)
@END9.on_message(group=2)
@END10.on_message(group=2)
async def raid_cwf_plug(_, m):
    await raid_cwf(_, m)

print("\n[module] loaded :- raid_cwf")

END.start()
print("\nEND1 STARTED !")
END2.start()
print("\nEND2 STARTED !")
END3.start()
print("\nEND3 STARTED !")
END4.start()
print("\nEND4 STARTED !")
END5.start()
print("\nEND5 STARTED !")
END6.start()
print("\nEND6 STARTED !")
END7.start()
print("\nEND7 STARTED !")
END8.start()
print("\nEND8 STARTED !")
END9.start()
print("\nEND9 STARTED !")
END10.start()
print("\nEND10 STARTED !")
print("\n\nALL CLIENTS STARTED SUCCESSFULLY !\nJoin @SpLBots")
idle()
