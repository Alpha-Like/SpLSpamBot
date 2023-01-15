from . import db

echo = db.echo

async def add_echo(user_id: int):
    x = await echo.find_one({"user_id": user_id})
    if not x:
        await echo.insert_one({"user_id": user_id})
    
async def del_echo(user_id: int):
    x = await echo.find_one({"user_id": user_id})
    if x:
        await echo.delete_one({"user_id": user_id})
    
async def is_echo(user_id: int):
    x = await echo.find_one({"user_id": user_id})
    if not x:
        return False
    return True

async def get_echos():
    x = echo.find({"user_id": {"$gt": 0}})
    if not x:
        return []
    echos = []
    for y in await x.to_list(length=1000000000):
        echos.append(y["user_id"])
    return echos
    
