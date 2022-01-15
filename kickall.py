import time
from random import shuffle

from pyrogram import Client
from pyrogram.types import ChatPermissions
from pyrogram.errors import FloodWait
from plugins.help import module_list; file_list; filters

@Client.on_message(filters.command('kickall', prefixes='!') & filters.me)
async def kickall(client, message):
        await message.edit("**Кикаем всех пользователей...**")
        members = [
        x
        for x in app.iter_chat_members(message.chat.id)
        if x.status not in ("administrator", "creator")
    ]
    shuffle(members)
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
        except FloodWait as e:
            time.sleep(e.x)
    await message.edit("**Все юзеры кикнуты.**")
