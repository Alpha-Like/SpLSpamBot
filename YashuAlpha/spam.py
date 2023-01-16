from .data import KeshavX, GROUP
from config import STUFF
import asyncio
from .verify import verify

hl = STUFF.COMMAND_HANDLER

SPAM = False

STOP = True

async def get_reply_and_args(m):
    reply = m.reply_to_message
    if not len(m.command) > 1:
        args = None
    else:
        args = m.text.split(None, 1)[1]
    if not reply:
        type = None 
    elif reply.photo:
        type = "photo"
    elif reply.video:
        type = "video"
    elif reply.animation:
        type = "animation"
    elif reply.document:
        type = "document"
    elif reply.audio:
        type = "audio"
    elif reply.voice:
        type = "voice"
    elif reply.sticker:
        type = "sticker"
    elif reply.text:
        type = "text"
    else:
        type = None
    if reply:
        if reply.caption:
            type += "-caption"
    return type, args

async def spam_func(_, m):
    if not await verify(m.from_user.id):
        return
    global SPAM, STOP
    STOP = False
    SPAM = True
    reply = m.reply_to_message
    a, b = await get_reply_and_args(m)
    if not a and not b:
        return await m.reply(f"`{hl}spam [either reply or give some text]`")
    if not b:
        return await m.reply(f"`{hl}spam [count] [text]`")
    if not a:
        try:
            count = int(b.split()[0])
        except:
            return await m.reply(f"`{hl}spam [count] [text]`")
        try:
            txt = b.split(None, 1)[1]
        except:
            return await m.reply(f"`{hl}spam [count] [text]`")
        for u in range(0, count):
            await _.send_message(m.chat.id, txt)
        return
    if a[-7:] == "caption":
        caption = True
        txt = reply.caption
    else:
        caption = False
    type = a.split("-")[0]
    try:
        count = int(b.split()[0])
    except:
        return await m.reply(f"`{hl}spam [count] [text]`")
    if not caption:
        try:
            txt = b.split(None, 1)[1]
            caption = True
        except:
            pass
    blank = ""
    if type == "photo":
        id = reply.photo.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_photo(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "video":
        id = reply.video.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_video(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "document":
        id = reply.document.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_document(m.chat.id, id, caption=f"{txt if caption else blank}", force_document=True)
    elif type == "animation":
        id = reply.animation.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_animation(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "voice":
        id = reply.voice.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_voice(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "audio":
        id = reply.audio.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_audio(m.chat.id, id, caption=f"{txt if caption else blank}")
    elif type == "text":
        id = reply.text
        for u in range(0, count):
            if STOP:
                return
            await _.send_message(m.chat.id, id)
    elif type == "sticker":
        id = reply.sticker.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_sticker(m.chat.id, id)
    STOP = True
    SPAM = False

async def dspam_func(_, m):
    if not await verify(m.from_user.id):
        return
    global SPAM, STOP
    STOP = False
    SPAM = True
    reply = m.reply_to_message
    a, b = await get_reply_and_args(m)
    if not a and not b:
        return await m.reply(f"`{hl}dspam [either reply or give some text]`")
    if not b:
        return await m.reply(f"`{hl}dspam [delay] [count] [text]`")
    if not a:
        try:
            delay = int(b.split()[0])
            count = int(b.split()[1])
        except:
            return await m.reply(f"`{hl}dspam [delay] [count] [text]`")
        try:
            txt = b.split(None, 2)[2]
        except:
            return await m.reply(f"`{hl}dspam [delay] [count] [text]`")
        for u in range(0, count):
            await _.send_message(m.chat.id, txt)
            await asyncio.sleep(delay)
        return
    if a[-7:] == "caption":
        caption = True
        txt = reply.caption
    else:
        caption = False
    type = a.split("-")[0]
    try:
        delay = int(b.split()[0])
        count = int(b.split()[1])
    except:
        return await m.reply(f"`{hl}dspam [delay] [count] [text]`")
    if not caption:
        try:
            txt = b.split(None, 2)[2]
            caption = True
        except:
            pass
    blank = ""
    if type == "photo":
        id = reply.photo.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_photo(m.chat.id, id, caption=f"{txt if caption else blank}")
            await asyncio.sleep(delay)
    elif type == "video":
        id = reply.video.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_video(m.chat.id, id, caption=f"{txt if caption else blank}")
            await asyncio.sleep(delay)
    elif type == "document":
        id = reply.document.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_document(m.chat.id, id, caption=f"{txt if caption else blank}", force_document=True)
            await asyncio.sleep(delay) 
    elif type == "animation":
        id = reply.animation.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_animation(m.chat.id, id, caption=f"{txt if caption else blank}")
            await asyncio.sleep(delay)
    elif type == "voice":
        id = reply.voice.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_voice(m.chat.id, id, caption=f"{txt if caption else blank}")
            await asyncio.sleep(delay)
    elif type == "audio":
        id = reply.audio.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_audio(m.chat.id, id, caption=f"{txt if caption else blank}")
            await asyncio.sleep(delay)
    elif type == "text":
        id = reply.text
        for u in range(0, count):
            if STOP:
                return
            await _.send_message(m.chat.id, id)
            await asyncio.sleep(delay)
    elif type == "sticker":
        id = reply.sticker.file_id
        for u in range(0, count):
            if STOP:
                return
            await _.send_sticker(m.chat.id, id)
            await asyncio.sleep(delay)
    STOP = True
    SPAM = False

async def spam_stop(_, m):
    if not await verify(m.from_user.id):
        return
    global SPAM, STOP
    if not SPAM:
        return await m.reply("`No ongoing spam...`")
    STOP = True
    SPAM = False
    return await m.reply("`Terminated...`")
