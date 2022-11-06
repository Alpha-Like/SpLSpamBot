from pyrogram import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import DEV, STUFF
import time

hl = STUFF.COMMAND_HANDLER

START_MARKUP_STR = IKM(
               [
               [
               IKB("💭 Owner 💭", url="t.me/Asynchorous"),
               IKB("✨ Support ✨", url="t.me/The_Hades_World")
               ],
               [
               IKB("🔥 Repo 🔥", url="https://github.com/Timeisnotwaiting/EndSpamBot)
               ]
               ]
               )

START_MARKUP_DEV = IKM(
               [
               [
               IKB("💫 Commands 💫", callback_data="cmds"),
               IKB("💭 Support 💭", url="t.me/The_Hades_World")
               ]
               ]
               )  


async def start(_, m):
    DEV.SUDO_USERS.append(DEV.OWNER_ID)
    x = DEV.SUDO_USERS
    bot_name = "𝙀𝙣𝙙 𝙓 𝙎𝙥𝙖𝙢"
    if m.from_user.id in x:
        txt = f"**Hello Boss !!, It's Me {bot_name}, Your Spam Bot !! \n\n Click Below Buttons For Help. 🌚**"
        await m.reply_photo(STUFF.START_PIC, caption=txt, START_MARKUP_DEV)
        return
    if str(m.chat.id)[0] == "-":
        return
    men = m.from_user.mention
    txt = f"**Hello !! {men}\nNice To Meet You, Well I Am {bot_name}, A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [𝙃𝙖𝙙𝙚𝙨](https://t.me/The_Hades_World)**"
    await m.reply_photo(STUFF.START_PIC, caption=txt, reply_markup=START_MARKUP_STR)
    return

HELP_TEXT = "★ 𝙀𝙣𝙙 𝙓 𝙎𝙥𝙖𝙢 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"

SPAM_HELP = spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

** © @Asynchorous**
"""

RAID_HELP = f"""
**Help Raid Cmds**

**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>

**DelayRaid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}delayraid <delay> <count> <Username of User>
2) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @Asynchorous**
"""

EXTRA_HELP = f"""
**Help Extra Cmds**

**Alive and Ping :** Ping Cmds
Command :
1) {hl}ping 
2) {hl}alive

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave :** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**© @Asynchorous**
"""

HELP_MARKUP = IKM(
              [
              [
              IKB("⚡️ Spam ⚡️", callback_data="spam_help"),
              IKB("🔥 Raid 🔥", callback_data="raid_help")
              ],
              [
              IKB("💭 Extras 💭", callback_data="extra_help")
              ],
              [
              IKB("😶‍🌫️ Owner 😶‍🌫️", url="t.me/Asynchorous"),
              IKB("✨ Support ✨", url="t.me/The_Hades_World")
              ]
              ]
              )

async def help(_, m):
    await m.reply_photo(STUFF.HELP_PIC, caption=HELP_TEXT, reply_markup=HELP_MARKUP)
    return

CLOSE_MARKUP = IKM(
               [
               [
               IKB("🗑️ Close", callback_data="close")
               ]
               ]
               )

async def cmds_cbq(_, q):
    await q.edit_message_text(text=HELP_TEXT, reply_markup=HELP_MARKUP)

async def spam_cbq(_, q):
    await q.edit_message_text(text=SPAM_HELP, reply_markup=CLOSE_MARKUP)

async def raid_cbq(_, q):
    await q.edit_message_text(text=RAID_HELP, reply_markup=CLOSE_MARKUP)

async def extra_cbq(_, q):
    await q.edit_message_text(text=EXTRA_HELP, reply_markup=CLOSE_MARKUP)

async def close_cbq(_, q):
    await q.message.delete()

