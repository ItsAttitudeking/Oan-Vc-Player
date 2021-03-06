from os import path

from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from youtube_search import YoutubeSearch

from callsmusic import callsmusic, queues

import converter
import youtube
import requests
import aiohttp
import wget

from helpers.database import db, Database
from helpers.dbthings import handle_user_status
from config import DURATION_LIMIT, LOG_CHANNEL, BOT_USERNAME, THUMB_URL, ZAID_QUE
from helpers.errors import DurationLimitError
from helpers.filters import command, other_filters
from helpers.decorators import errors
from converter.converter import convert
from . import que


@Client.on_message(filters.private)
async def _(bot: Client, cmd: command):
    await handle_user_status(bot, cmd)


# Some Secret Buttons
PLAYMSG_BUTTONS = InlineKeyboardMarkup(
    [
            [
                InlineKeyboardButton("β‘ππββπβπβ‘", url=f"https://t.me/OAN_Support"),
                InlineKeyboardButton("π₯πβπ»πΈππΌππ₯", url=f"https://t.me/Attitude_Network"),
            ],
            [InlineKeyboardButton("πΉοΈβππππΌπΉοΈ", callback_data="close")],
        ]
)


@Client.on_message(command(["audioplay", f"stream"]) & other_filters)
@errors
async def play(_, message: Message):
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None

    response = await message.reply_text("π")

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Ι΄α΄α΄α΄: κ±α΄Ι΄Ι’ Ι΄α΄α΄ Κα΄Ι΄Ι’α΄Κ α΄Κα΄Ι΄ `{DURATION_LIMIT}` π€¨"
            )

        file_name = audio.file_unique_id + "." + (
            (
                audio.file_name.split(".")[-1]
            ) if (
                not isinstance(audio, Voice)
            ) else "ogg"
        )

        file = await converter.convert(
            (
                await message.reply_to_message.download(file_name)
            )
            if (
                not path.isfile(path.join("downloads", file_name))
            ) else file_name
        )
    else:
        messages = [message]
        text = ""
        offset = None
        length = None

        if message.reply_to_message:
            messages.append(message.reply_to_message)

        for _message in messages:
            if offset:
                break

            if _message.entities:
                for entity in _message.entities:
                    if entity.type == "url":
                        text = _message.text or _message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset in (None,):
            await response.edit_text(f"`Lol! You did not give me anything to play!`")
            return

        url = text[offset:offset + length]
        file = await converter.convert(youtube.download(url))

    if message.chat.id in callsmusic.active_chats:
        thumb = ZAID_QUE
        position = await queues.put(message.chat.id, file=file)
        MENTMEH = message.from_user.mention()
        await response.delete()
        await message.reply_photo(thumb, caption=f"**Your Song Queued at position** `{position}`! \n**Requested by: {MENTMEH}**", reply_markup=PLAYMSG_BUTTONS)
    else:
        thumb = THUMB_URL
        await callsmusic.set_stream(message.chat.id, file)
        await response.delete()
        await message.reply_photo(thumb, caption="**Playing Your Song π§...** \n**Requested by: {}**".format(message.from_user.mention()), reply_markup=PLAYMSG_BUTTONS)


#what u want ? Kis lie aaya BSDK ....
@Client.on_message(command(["play", f"ytplay"]) & other_filters)
@errors
async def nplay(_, message: Message):

    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("πβπ»πΈππΌπ", url=f"https://t.me/Attitude_Network")
            ],[
                InlineKeyboardButton("πΉοΈβππππΌπΉοΈ", callback_data="close")
            ]
        ]
    )
    
    nofound = "π **Ιͺ α΄Ιͺα΄Ι΄'α΄ α΄ΚΚα΄ α΄α΄ κ°ΙͺΙ΄α΄ α΄Κ κ±α΄Ι΄Ι’ α΄Κα΄’ α΄α΄α΄α΄ α΄α΄ΚΚα΄α΄α΄ κ±α΄α΄ΚΚ α΄Κα΄Κα΄**"


    global que
    
    lel = await message.reply_text("β‘")
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    query = ""
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        await lel.edit(
            f"**Error:** {e}"
        )
        print(str(e))
        return
    try:    
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        if (dur / 60) > DURATION_LIMIT:
             await lel.edit(f"Ι΄α΄α΄α΄: κ±α΄Ι΄Ι’ Ι΄α΄α΄ Κα΄Ι΄Ι’α΄Κ α΄Κα΄Ι΄ `{DURATION_LIMIT}` π")
             return
    except:
        pass    

    file = await convert(youtube.download(url))
    if message.chat.id in callsmusic.active_chats:
        thumb = ZAID_QUE
        position = await queues.put(message.chat.id, file=file)
        MENTMEH = message.from_user.mention()
        await lel.delete()
        await message.reply_photo(thumb, caption=f"**Your Song Queued at position** `{position}`! \n**Requested by: {MENTMEH}**", reply_markup=PLAYMSG_BUTTONS)
    else:
        thumb = THUMB_URL
        await callsmusic.set_stream(message.chat.id, file)
        await lel.delete()
        await message.reply_photo(thumb, caption="**βοΈα΄Κα΄ΚΙͺΙ΄Ι’...** \n**α΄κ±α΄Κ ΚΚ: {}**".format(message.from_user.mention()), reply_markup=PLAYMSG_BUTTONS)
