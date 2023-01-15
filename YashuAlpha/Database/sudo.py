from . import db

sudodb = db.sudo

async def add_sudo(user_id: int):
    sudo = await sudodb.find_one({"user_id": user_id})
    if sudo:
        return
    return await sudodb.insert_one({"user_id": user_id})

async def del_sudo(user_id: int):
    sudo = await sudodb.find_one({"user_id": user_id})
    if not sudo:
        return
    return await sudodb.delete_one({"user_id": user_id})

async def is_sudo(user_id: int):
    sudo = await sudodb.find_one({"user_id": user_id})
    if sudo:
        return True
    return False

async def get_sudos():
    sudos = sudodb.find({"user_id": {"$gt": 0}})
    if not sudos:
        return []
    SUDOS = []
    for _ in await sudos.to_list(length=1000000000):
        SUDOS.append(_["user_id"])
    return SUDOS
