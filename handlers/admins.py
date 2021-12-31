import traceback
import asyncio # Lol! Weird Import!

from asyncio import QueueEmpty

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic import callsmusic, queues

from helpers.filters import command
from helpers.decorators import errors, authorized_users_only
from helpers.database import db, dcmdb, Database
from helpers.dbthings import handle_user_status, delcmd_is_on, delcmd_on, delcmd_off
from config import LOG_CHANNEL, BOT_OWNER, BOT_USERNAME
from . import que, admins as fuck


@Client.on_message()
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

# Back Button
BACK_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Go Back ⬅️", callback_data="cbback")]])

# @Client.on_message(~filters.private)
async def delcmd(_, message: Message):
    if await delcmd_is_on(message.chat.id) and message.text.startswith("/") or message.text.startswith("!"):
        await message.delete()
    await message.continue_propagation()


@Client.on_message(filters.command(["reload", f"adminchache"]))
@authorized_users_only # Fuk Off Everyone! Admin Only Command!
async def update_admin(client, message):
    global fuck
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    new_ads = []
    for u in admins:
        new_ads.append(u.user.id)
    fuck[message.chat.id] = new_ads
    await message.reply_text("**𝔸𝕕𝕞𝕚𝕟 𝕃𝕚𝕤𝕥 𝕊𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪 𝕌𝕡𝕕𝕒𝕥𝕖𝕕✅!**")


# Control Menu Of Player
@Client.on_message(command(["control", f"controlpanel", "p"]))
@errors
@authorized_users_only
async def controlset(_, message: Message):
    await message.reply_text(
        "**ℂ𝕠𝕟𝕥𝕣𝕠𝕝 ℙ𝕒𝕟𝕖𝕝 𝕊𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝𝕝𝕪 𝕆𝕡𝕖𝕟𝕖𝕕🎧!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ℙ𝔸𝕌𝕊𝔼 ⏸️", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "ℝ𝔼𝕊𝕌𝕄𝔼 ▶️", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝕊𝕂𝕀ℙ ⏩", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "𝔼ℕ𝔻 ⏹", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝕄𝕌𝕋𝔼 🔈", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "𝕌ℕ𝕄𝕌𝕋𝔼 🔊", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )



@Client.on_message(command(["pause", f"pause@{BOT_USERNAME}", "p"]))
@errors
@authorized_users_only
async def pause(_, message: Message):
    if callsmusic.pause(message.chat.id):
        await message.reply_text("⏸️ 𝕊𝕌ℂℂ𝔼𝕊𝕊𝔽𝕌𝕃𝕃𝕐 ℙ𝔸𝕌𝕊𝔼𝔻")
    else:
        await message.reply_text("🧐 ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾")

@Client.on_message(command(["resume", f"resume@{BOT_USERNAME}", "r"]))
@errors
@authorized_users_only
async def resume(_, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text("🎧 𝕊𝕌ℂℂ𝔼𝕊𝕊𝔽𝕌𝕃𝕃𝕐 ℝ𝔼𝕊𝕌𝕄𝔼𝔻")
    else:
        await message.reply_text("🧐 ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾")


@Client.on_message(command(["end", f"end@{BOT_USERNAME}", "stop"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("🧐 ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾")
    else:
        try:
            queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(message.chat.id)
        await message.reply_text("✅ℂ𝕝𝕖𝕒𝕣 𝕥𝕙𝕖 ℚ𝕦𝕖𝕦𝕖 𝕒𝕟𝕕 𝕝𝕖𝕗𝕥 𝕥𝕙𝕖 𝕍𝕠𝕚𝕔𝕖 ℂ𝕙𝕒𝕥!")


@Client.on_message(command(["skip", f"next", "s"]))
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.active_chats:
        await message.reply_text("🧐 ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            await callsmusic.stop(message.chat.id)
        else:
            await callsmusic.set_stream(
                message.chat.id, queues.get(message.chat.id)["file"]
            )

        await message.reply_text("𝕊𝕜𝕚𝕡𝕡𝕖𝕕 ⏩")


@Client.on_message(command(["mute", f"mute@{BOT_USERNAME}", "m"]))
@errors
@authorized_users_only
async def mute(_, message: Message):
    result = callsmusic.mute(message.chat.id)

    if result == 0:
        await message.reply_text("🔇 𝕄𝕌𝕋𝔼𝔻")
    elif result == 1:
        await message.reply_text("🔇 𝔸𝕝𝕣𝕖𝕒𝕕𝕪 𝕞𝕦𝕥𝕖𝕕")
    elif result == 2:
        await message.reply_text("‼️ ℕ𝕠𝕥 𝕚𝕟 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥")


@Client.on_message(command(["unmute", f"unmute@{BOT_USERNAME}", "um"]))
@errors
@authorized_users_only
async def unmute(_, message: Message):
    result = callsmusic.unmute(message.chat.id)

    if result == 0:
        await message.reply_text("🔈 𝕌𝕟𝕞𝕦𝕥𝕖𝕕")
    elif result == 1:
        await message.reply_text("🔈 𝔸𝕝𝕣𝕖𝕒𝕕𝕪 𝕌𝕟𝕞𝕦𝕥𝕖𝕕")
    elif result == 2:
        await message.reply_text("‼️ ℕ𝕠𝕥 𝕚𝕟 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥")


# Music Player Callbacks (Control by buttons feature)

@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if callsmusic.pause(query.message.chat.id):
        await query.edit_message_text("⏸ 𝕊𝕠𝕟𝕘 ℙ𝕒𝕦𝕤𝕖𝕕", reply_markup=BACK_BUTTON)
    else:
        await query.edit_message_text("‼️ ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if callsmusic.resume(query.message.chat.id):
        await query.edit_message_text("🎧 𝕊𝕠𝕟𝕘 ℝ𝕖𝕤𝕦𝕞𝕖𝕕", reply_markup=BACK_BUTTON)
    else:
        await query.edit_message_text("‼️ ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾!", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbend"))
async def cbend(_, query: CallbackQuery):
    if query.message.chat.id not in callsmusic.active_chats:
        await query.edit_message_text("‼️ ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾", reply_markup=BACK_BUTTON)
    else:
        try:
            queues.clear(query.message.chat.id)
        except QueueEmpty:
            pass

        await callsmusic.stop(query.message.chat.id)
        await query.edit_message_text("✅ ℂ𝕝𝕖𝕒𝕣 𝕥𝕙𝕖 ℚ𝕦𝕖𝕦𝕖 𝕒𝕟𝕕 𝕝𝕖𝕗𝕥 𝕥𝕙𝕖 𝕍𝕠𝕚𝕔𝕖 ℂ𝕙𝕒𝕥!", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbskip"))
async def cbskip(_, query: CallbackQuery):
     if query.message.chat.id not in callsmusic.active_chats:
        await query.edit_message_text("‼️ ℕ𝕆𝕋ℍ𝕀ℕ𝔾 𝕀𝕊 ℙ𝕃𝔸𝕐𝕀ℕ𝔾", reply_markup=BACK_BUTTON)
     else:
        queues.task_done(query.message.chat.id)
        
        if queues.is_empty(query.message.chat.id):
            await callsmusic.stop(query.message.chat.id)
        else:
            await callsmusic.set_stream(
                query.message.chat.id, queues.get(query.message.chat.id)["file"]
            )

        await query.edit_message_text("𝕊𝕜𝕚𝕡𝕡𝕖𝕕 ⏩", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    result = callsmusic.mute(query.message.chat.id)

    if result == 0:
        await query.edit_message_text("🔇 𝕄𝕌𝕋𝔼𝔻", reply_markup=BACK_BUTTON)
    elif result == 1:
        await query.edit_message_text("🔇 𝔸𝕝𝕣𝕖𝕒𝕕𝕪 𝕞𝕦𝕥𝕖𝕕", reply_markup=BACK_BUTTON)
    elif result == 2:
        await query.edit_message_text("‼️ ℕ𝕠𝕥 𝕚𝕟 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥", reply_markup=BACK_BUTTON)

@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    result = callsmusic.unmute(query.message.chat.id)

    if result == 0:
        await query.edit_message_text("🔈 𝕌𝕟𝕞𝕦𝕥𝕖𝕕", reply_markup=BACK_BUTTON)
    elif result == 1:
        await query.edit_message_text("🔈𝔸𝕝𝕣𝕖𝕒𝕕𝕪 𝕌𝕟𝕞𝕦𝕥𝕖𝕕", reply_markup=BACK_BUTTON)
    elif result == 2:
        await query.edit_message_text("‼️ ℕ𝕠𝕥 𝕚𝕟 𝕧𝕠𝕚𝕔𝕖 𝕔𝕙𝕒𝕥", reply_markup=BACK_BUTTON)


# Anti-Command Feature On/Off

@Client.on_message(filters.command(["delcmd", f"delcmd@{BOT_USERNAME}"]) & ~filters.private)
@authorized_users_only
async def delcmdc(_, message: Message):
    if len(message.command) != 2:
        await message.reply_text("Lol! This isn't the way to use this command 😂! Please read **/help** ☺️ Any problem @OAN_Support")
        return
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on":
        if await delcmd_is_on(message.chat.id):
            await message.reply_text("Eh! You are already enabled This Service 😉 Any problem ask @OAN_Support ")
            return
        else:
            await delcmd_on(chat_id)
            await message.reply_text(
                "Successfully Enabled Delete Command Feature For This Chat 😇 Any problem ask @OAN_Support"
            )
    elif status == "off":
        await delcmd_off(chat_id)
        await message.reply_text("Successfully Disabled Delete Command Feature For This Chat 😌 Any problem ask @OAN_Support")
    else:
        await message.reply_text(
            "Can't Understand What you're talking about! Maybe Read **/help** 🤔 Any problem ask @OAN_Support"
        )
