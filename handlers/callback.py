from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, UPDATES_CHANNEL

# close calllback

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# Player Control Callbacks

@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**Here is The Control Menu Of Streamer!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βΈ βπΈπππΌ βΈ", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "βΆοΈ βπΌππππΌ βΆοΈ", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β© πππβ β©", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "βΉ πΌβπ» βΉ", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π ππππΌ π", callback_data="cbmute"
                    ),
                    InlineKeyboardButton(
                        "π πβππππΌ π", callback_data="cbunmute"
                    )
                ]
            ]
        )
    )


# Start callback 

@Client.on_callback_query(filters.regex("cbstart"))
async def startcb(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} ποΈ!</b>

I'm The OAN Music Bot! A Powerful Bot to Play Music in Your Group Voice Chat π!

Also I have more features! Please hit on **/help** to see them π!

Made with β€οΈ **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βπΈπ»π» ππΌ  ππ πβ πΎβππββ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "βπΌπβπ?ββοΈ", callback_data="cbhelpmenu"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β¬ππβπΌββ¬", url="Https://t.me/ItsAttitudeking"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πβπ»πΈππΌππ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ππββπβπποΈ", url="https://t.me/OAN_Support"
                    )
                ]
            ]
        )
    )
    

# Help Callback Menu

@Client.on_callback_query(filters.regex("cbhelpmenu"))
async def cbhelpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hi {query.message.from_user.mention} ποΈ!</b>

**βππ£π ππ€ π₯ππ βπππ‘ ππππ¦ π½π π£ ππππ€ πΉπ π₯βΌοΈ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βππ ππ πππΌ ππΌπ", callback_data="cbhowtouse"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "βπ¦π π₯πππͺ", callback_data="cbquotely"
                    )
                ]
            ]
        )
    )

# How to Use Module Help

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbhowtouse(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>How To Use This Bot?</b>

**πππ₯π₯πππ ππ‘ πππ πΉπ π₯:**
    1. Add **{BOT_USERNAME}** Bot and @{(await USER.get_me()).username} To Your Group! (Send `/userbotjoin` to your group! Streamer Will Automatically join)
    2. Give Admin To **{BOT_USERNAME}** and **@{(await USER.get_me()).username}** !

 
**Using Player Commands:**
    1. **Group Admin Only Commands π? ,**
     - `/stream` - Reply to supported url, Reply to Audio File or Send `/stream` with [Supported Url](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
       **Example:** `/stream https://www.youtube.com/watch?v=ALZHF5UqnU4`
        
     - `/play` - Play Song by Name. (Currenty Supported for Youtube Only)
       **Example:** `/play amplifier`
    
     - `/skip` - Skip currenly playing song.
    
     - `/pause` - Pause currently playing song.
    
     - `/resume` - Resume currently pushed song.
    
     - `/mute` - Mutes Streamer.
    
     - `/unmute`- Unmutes streamer.
     
     - `/end` - Stop playing and leaves the voice chat.
    
     - `/userbotjoin` - To Add Streamer Account To Your Group.
    
     - `/leavegrp` - To Remove Streamer Account From Your Group.
     
     - `/control` - To Control the Streamer Account in VC by Buttons. (Like pause, resume, skip etc.)
     
    2. **Other Commands,**
     - `/vc` - To Get and Share Voice Chat Link. (Public Groups Only)


**ππ¦π‘π‘π π£π₯ππ πβπ πππ€π₯:** Β©οΈ @Attitude_Network

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        ),
        disable_web_page_preview = True
    )


# Lyrics Module Help

@Client.on_callback_query(filters.regex("cbgetlyrics"))
async def cbgetlyrics(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Lyrics Plugin</b>

**Feature:** Get Lyrics For Provided Song Name!

**Usage:**
    - Send Your Song Name with `/lyrics` command.

**Example:** `/lyrics faded`

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Yt Search Module Help

@Client.on_callback_query(filters.regex("cbytsearch"))
async def cbytsearch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For YT Search Plugin</b>

**Feature:** Search Youtube Videos Inline or Using a Command!

**Usage:**
    1. For Inline Search Feature,
     - Type `@{BOT_USERNAME}` in any chat then type ` `(space) and search.
    
    2. For Search Via Command,
     - Send `/search` command with your keyword.

**Example:**
    1. Example For Inline Search
     - `@{BOT_USERNAME} faded`
    
    2. Example For Search via Command
     - `/search faded`

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
    
    
# Music Downloader Help

@Client.on_callback_query(filters.regex("cbmusicdown"))
async def cbmusicdown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Music Downloader Plugin</b>

**Feature:** Download Music As Audio From YouTube, Saavn, Deezer

**Usage:**
    1. For Youtube Audio Download,
      - Send Your Song Name with `/yts` command.
    
    2. For Saavn Audio Download,
      - Send Your Song Name with `/saavn` command.
    
    3. For Deezer Audio Download,
      - Send Your Song Name with `/deezer` command.

**Example:**
    1. Example For Youtube Audio Download,
      - `/yts alone`
    
    2. Example For Saavn Audio Download,
      - `/saavn faded`
    
    3. Example For Deezer Audio Download,
      - `/deezer unity`

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# YT Video Downloader Help

@Client.on_callback_query(filters.regex("cbytviddown"))
async def cbytviddown(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For YT Video Downloader Plugin</b>

**Feature:** Download Youtube Videos For Provided Name!

**Usage:**
    - Send Your Youtube Video Name with `/ytvid` command.

**Example:** `/video Waalian Remix`

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Delete Command Help

@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Delete Command Plugin</b>

**Feature:** Delete Every Commands Sent By Users to Avoid Spam in Your Group!

**Usage:**
    1. To Turn On This,
      - Send `/delcmd on` command.
    
    2. To Turn Off This,
      - Send `/delcmd off` command.

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βοΈ  πΉπππ βοΈ", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )


# Quotely Help

@Client.on_callback_query(filters.regex("cbquotely"))
async def cbquotely(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Help For Quotely Plugin</b>

**Feature:** Quote Messages Like Quotely Bot!

**Usage:**
    1. To Quote One Message,
      - `/q` reply to a text message
      
    2. To Quote More Than One Message,
      - `/q` [Integer] reply to a text message
     
    3. To Quote Message with Reply
      - `/q r` reply to a text message

**Example:**
    1. Example Quote One Message,
      - `/q` reply to a text message
      
    2. Example Quote More Than One Message,
      - `/q 2` reply to a text message
     
    3. Example Quote Message with Reply,
      - `/q r` reply to a text message

Made with β€οΈ by **@{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β« πΉπππ β¬", callback_data="cbhelpmenu"
                    )
                ]
            ]
        )
    )
