from .data import KeshavX, GROUP
from config import STUFF
import asyncio

hl = STUFF.COMMAND_HANDLER

async def spam(_, m):
    if m.chat.id in GROUP:
        return await m.reply("CAN'T SPAM IN OWNER's GROUP ! 🌝✨")
    if str(m.chat.id)[0] != "-":
        return await m.reply("THIS COMMAND ONLY WORKS IN GROUP ! 🌝✨")
    y = m.reply_to_message
    if y:
        txt = None
        if y.photo:
            x = await _.download_media(y)
            try:
                count = int(m.text.split()[1])
            except:
                return await m.reply(f"{hl}spam [count]")
        elif y.sticker:
            x = y.sticker.id
            try:
                count = int(m.text.split()[1])
            except:
                return await m.reply(f"{hl}spam [count]")
        elif y.video:
            x = await _.download_media(y)
            try:
                txt = m.text.split(None, 1)[1]
            except:
                txt = None  
        elif y.document:
            x = await _.download_media(y)
            try:
                count = int(m.text.split()[1])
            except:
                return await m.reply(f"{hl}spam [count]")
        elif y.audio:
            x = await _.download_media(y)
            try:
                count = int(m.text.split()[1])
            except:
                return await m.reply(f"{hl}spam [count]")
        else:
            x = None
            try:
                count = int(m.text.split()[1])
                txt = m.text.split(None, 1)[2]
            except:
                return await m.reply(f"{hl}spam [count] [text]")
    else:
        try:
            count = int(m.text.split()[1])
            txt = m.text.split(None, 1)[2]
        except:
            return await m.reply(f"{hl}spam [count] [text]")

    for x in range(0, count):
        if y.photo:
            try:
                await _.send_photo(m.chat.id, x)
            except Exception as e:
                print(e)
                pass
        elif y.video:
            try:
                await _.send_video(m.chat.id, x)
            except Exception as e:
                print(e)
                pass
        elif y.audio:
            try:
                await _.send_audio(m.chat.id, x)
            except Exception as e:
                print(e)
                pass
        elif y.document:
            try:
                await _.send_document(m.chat.id, x)
            except Exception as e:
                print(e)
                pass
        else:
            try:
                await _.send_message(m.chat.id, txt)
            except Exception as e:
                print(e)
                pass
        
        
        
        
