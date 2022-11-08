from pyrogram import Client, filters, idle
from config import *
import time
from YashuAlpha.plugins import start, help, cmds_cbq, close_cbq, raid_cbq, extra_cbq, spam_cbq
from YashuAlpha.raid import raid, replyraid, dreplyraid, raid_cwf
from YashuAlpha.data import KeshavX
from YashuAlpha.spam import spam, dspam
from YashuAlpha.echo import addecho, rmecho, echo_cwf
from YashuAlpha.leave import leave

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)
END2 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_2)
END3 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_3)
END4 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_4)
END5 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_5)
END6 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_6)
END7 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_7)
END8 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_8)
END9 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_9)
END10 = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN_10)

@END.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("help", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("help", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("help", hl) & filters.user(LEGENDS))
async def help_plug(_, m):
    await help(_, m)

print("[module] loaded :- help")

@END.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("spam", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("spam", hl) & filters.user(LEGENDS))
async def spam_plug(_, m):
    await spam(_, m)

print("\n[module] loaded :- spam")

@END.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("dspam", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("dspam", hl) & filters.user(LEGENDS))
async def dspam_plug(_, m):
    await dspam(_, m)

print("\n[module] loaded :- dspam")

@END.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("addecho", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("addecho", hl) & filters.user(LEGENDS))
async def addecho_plug(_, m):
    await addecho(_, m)

print("\n[module] loaded :- addecho")

@END.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END2.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END3.on_message(filters.command("rmecho", hl)& filters.user(LEGENDS))
@END4.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END5.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END6.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END7.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END8.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END9.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
@END10.on_message(filters.command("rmecho", hl) & filters.user(LEGENDS))
async def rmecho_plug(_, m):
    await rmecho(_, m)

print("\n[module] loaded :- rmecho")

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

def Asynchorous():
    a = 1
    Clients = [END, END2, END3, END4, END5, END6, END7, END8, END9, END10]
    for x in Clients:
        if a == 11:
            break
        x.run()
        print(f":END{a}: started...!")
        a += 1

Asynchorous()
