import os
from os import getenv

from pyrogram import Client
from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . *   ,").split())

BOT_OWNER = int(os.environ.get("BOT_OWNER")) # Your Telegram User ID
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split())) # Sudo users IDs, They are admins everywhere
BOT_USERNAME = os.environ.get("BOT_USERNAME") # Your Bot's Username without "@"
DATABASE_URL = os.environ.get("DATABASE_URL") #mongo database url for more info contact in support group
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # Your Log Channel! Make a private channel and get it's ID
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # If you need to broadcast messages as a copy or Forwarded Message
THUMB_URL = os.environ.get("THUMB_URL", "https://telegra.ph/file/802f9a6b9f988b3cb7d40.jpg")
ZAID_QUE = os.environ.get("ZAID_QUE", "https://telegra.ph/file/3e4b6571b78cc07270e36.jpg")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Attitude_Network")
ZAID_SUPPORT = os.environ.get("OAN_SUPPORT", "Attitude_Network")

# SOON ADDING 
ARQ_API_KEY = getenv("ARQ_API_KEY")
# Don't Change Anything Here
ARQ_API_URL = "https://thearq.tech/"

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/itsunknown-12/Zaid-Vc-Player")
U_BRANCH = "master"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

# HEHE
z_version = "v2.0.2.1"
zaidub_version = "v2.0"
