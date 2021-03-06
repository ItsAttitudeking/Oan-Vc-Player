import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME, UPDATES_CHANNEL, ZAID_SUPPORT
from helpers.filters import command
from helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""**ππΌπβπππΌπ
β’βββββββ§ββ¦ββ§βββββββ’
βββββββββββββββββββ
β£βπ°πΈ πΈππ§πππππ ππππππ£ππ ππ¦π€ππ πΉπ π₯ π¨ππ₯π ππ π π π½πππ₯π¦π£ππ€........
β£βπ₯ππππππ€ ππ π£ π¦π€πππ β’πππ
β£βπππ¨π°ππ«ππ ππ² : [β‘πΈππππππ»πΌ βπΌπππβπβ‘](Https://t.me/Attitude_Network)
βββββββββββββββββββ
β’βββββββ§ββ¦ββ§βββββββ’
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ππΈπ»π» ππΌ ππ πΎβππβπ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ππββπβπποΈ", url=f"https://t.me/OAN_Support"
                    ),
                    InlineKeyboardButton(
                        "βοΈππβπΌββοΈ", url=f"@ItsAttitudeking"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πβπ»πΈππΌππ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "King"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""ππππππ€ ππ π£ πΈπππππ πππ₯π₯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π₯π₯ππ ππ πππ£π πππ π€π¦π‘π‘π π£π₯π₯π₯", url=f"https://t.me/Attitude_Network")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""π°π½π π£ ππ π£π ππ π₯π€ πππ π£ππ‘π  ππ ππ: @Attitude_Network""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π₯πΉβπΌβππΉπ₯", url=f"https://github.com/ItsAttitudeking")
                ]
            ]
        ),
    )
