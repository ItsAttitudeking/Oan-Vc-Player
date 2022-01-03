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
        caption=f"""**𝕎𝔼𝕃ℂ𝕆𝕄𝔼😜
•❅─────✧❅✦❅✧─────❅•
┏━━━━━━━━━━━━━━━━━┓
┣★🔰𝔸 𝔸𝕕𝕧𝕒𝕟𝕔𝕖𝕕 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 𝕄𝕦𝕤𝕚𝕔 𝔹𝕠𝕥 𝕨𝕚𝕥𝕙 𝕔𝕠𝕠𝕝 𝔽𝕖𝕒𝕥𝕦𝕣𝕖𝕤........
┣★🔥𝕋𝕙𝕒𝕟𝕜𝕤 𝕗𝕠𝕣 𝕦𝕤𝕚𝕟𝕘 ➢𝐎𝐀𝐍
┣★🔗𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : [⚡𝔸𝕋𝕋𝕀𝕋𝕌𝔻𝔼 ℕ𝔼𝕋𝕎𝕆ℝ𝕂⚡](Https://t.me/Attitude_Network)
┗━━━━━━━━━━━━━━━━━┛
•❅─────✧❅✦❅✧─────❅•
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔔𝔸𝔻𝔻 𝕄𝔼 𝕋𝕆 𝔾ℝ𝕆𝕌ℙ🔔", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝕊𝕌ℙℙ𝕆ℝ𝕋🛎️", url=f"https://t.me/OAN_Support"
                    ),
                    InlineKeyboardButton(
                        "⚜️𝕆𝕎ℕ𝔼ℝ⚜️", url=f"@ItsAttitudeking"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝕌ℙ𝔻𝔸𝕋𝔼𝕊🔊", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "King"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""𝕋𝕙𝕒𝕟𝕜𝕤 𝕗𝕠𝕣 𝔸𝕕𝕕𝕚𝕟𝕘 𝕞𝕖🔥🥂""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🥂𝕁𝕠𝕚𝕟 𝕙𝕖𝕣𝕖 𝕒𝕟𝕕 𝕤𝕦𝕡𝕡𝕠𝕣𝕥🥂🔥", url=f"https://t.me/Attitude_Network")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9560aa796165f09b35165.jpg",
        caption=f"""🔰𝔽𝕠𝕣 𝕞𝕠𝕣𝕖 𝕓𝕠𝕥𝕤 𝕒𝕟𝕕 𝕣𝕖𝕡𝕠 𝕛𝕠𝕚𝕟: @Attitude_Network""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥🍹ℝ𝔼ℙ𝕆🍹🔥", url=f"https://github.com/ItsAttitudeking")
                ]
            ]
        ),
    )
