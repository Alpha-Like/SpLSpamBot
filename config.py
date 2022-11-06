import os

class API:
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]

class TOKENS:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    BOT_TOKEN_2 = os.environ["BOT_TOKEN_2"]
    BOT_TOKEN_3 = os.environ["BOT_TOKEN_3"]
    BOT_TOKEN_4 = os.environ["BOT_TOKEN_4"]
    BOT_TOKEN_5 = os.environ["BOT_TOKEN_5"]
    BOT_TOKEN_6 = os.environ["BOT_TOKEN_6"]
    BOT_TOKEN_7 = os.environ["BOT_TOKEN_7"]
    BOT_TOKEN_8 = os.environ["BOT_TOKEN_8"]
    BOT_TOKEN_9 = os.environ["BOT_TOKEN_9"]
    BOT_TOKEN_10 = os.environ["BOT_TOKEN_10"]

class DEV:
    OWNER_ID = int(os.environ["OWNER_ID"])
    SUDO_USERS_STR = os.environ["SUDO_USERS"].split()
    SUDO_USERS = []
    for x in SUDO_USERS_STR:
        SUDO_USERS.append(int(x))

class STUFF:
    ALIVE_PIC = os.environ["ALIVE_PIC"]
    PING_PIC = os.environ["PING_PIC"]
