

import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "19071424"))
API_HASH = os.environ.get("API_HASH", "c4b3e298cc50fd4cc563ae75ee882948")


OWNER = os.environ.get("OWNER", "7425490417") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "7425490417")) #Owner user id
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")

PICS = (environ.get('PICS', 'https://telegra.ph/file/ee0cdd28fdd53d3df26c7.jpg https://telegra.ph/file/def62cc4e67aabc03d4c8.jpg https://telegra.ph/file/0c04c8e0b4a67d1716f53.jpg https://telegra.ph/file/eccd0bd3f18111afb9726.jpg https://telegra.ph/file/d6a99238948a8918e3e94.jpg https://telegra.ph/file/fcaf8e6dbadb19364ab54.jpg https://telegra.ph/file/6ca5d5dc24e029c4fe642.jpg https://telegra.ph/file/80a417b7cfc6dc262dcee.jpg https://telegra.ph/file/0426befe276a430a6cdf0.jpg https://telegra.ph/file/7d716533a70fad271a5b9.jpg')).split()


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001974433785"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002320550967"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "<b>𝖧𝖾𝗒 {mention} 𝖨 𝖠𝗆 𝗞𝗔𝗟𝗬𝗔𝗡𝗜, 𝖧𝖺𝗉𝗉𝗒 🖤 𝖳𝗈 𝖧𝖺𝗏𝖾 𝖸𝗈𝗎\n\n𝖨𝖺𝗆 𝖯𝗈𝗐𝖾𝗋𝖥𝗎𝗅𝗅 Private Files Store Private 𝖡𝗈𝗍 ⚙\n\n📌 𝗔𝗻𝘆 𝗛𝗲𝗹𝗽 𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗔𝗱𝗺𝗶𝗻 : @MCU_ADMIN_V1_BOT</b>")
try:
    ADMINS=[1297128957]
    for x in (os.environ.get("ADMINS", "7425490417").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first}\n\n♦️ READ THIS INSTRUCTION ♦️\n\n🗣 നിങ്ങൾ ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ 📢 Request to join Channel 📢 എന്ന ബട്ടണിലോ താഴെ കാണുന്ന ലിങ്കിലോ ക്ലിക്ക് ചെയ്യാവുന്നതാണ്. Join channel ക്ലിക്ക് ചെയ്ത ശേഷം 🔄 Try Again 🔄 എന്ന ബട്ടണിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ അയച്ചു തരുന്നതാണ്..😍\n\n🗣 In Order To Get The Movie Requested By You in Our Group, You Must Have To Join Our Official Channel First By Clicking 📢 Request to Join Channel 📢 Button or the Link shown Below. After That, Click 🔄 Try Again 🔄 Button. I'll Send You That Movie 🙈\n\n👇 CLICK REQUEST TO JOIN CHANNEL & CLICK TRY AGAIN 👇</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{previouscaption}\n\n╔═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╗\n➲ @MCUupdatesLINKS\n╚═══ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═══╝</b>")

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "False" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(7425490417)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
