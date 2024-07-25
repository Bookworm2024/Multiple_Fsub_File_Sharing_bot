#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21145186"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002160865517"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6011680723"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://infohubstore06:Mf8U56mbjVqeN3Gm@fileshare.ir0tgdu.mongodb.net/?retryWrites=true&w=majority&appName=fileshare")
DB_NAME = os.environ.get("DATABASE_NAME", "fileshare")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002123546604"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002170049626"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1001993667849"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002182645748"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ!! {mention} 👋\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ᴀɴᴅ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ɪɴꜰᴏʜᴜʙ ɴᴇᴛᴡᴏʀᴋꜱ.🍂💫\n\n⚠️ᴅᴏ ɴᴏᴛ ꜱᴇɴᴅ ᴍᴇ ᴅɪʀᴇᴄᴛ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰᴏʀ ɪ ᴀᴍ ɴᴏᴛ ᴅᴇꜱɪɢɴᴇᴅ ᴛᴏ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇᴍ!!⚠️")
try:
    ADMINS=[6011680723]
    for x in (os.environ.get("ADMINS", "6011680723 1524169222 2007123863 7000915053 6792991359").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐇𝐞𝐥𝐥𝐨, {mention}\n\n<b>𝐔𝐦𝐦, 𝐬𝐨𝐫𝐫𝐲 𝐭𝐨 𝐢𝐧𝐭𝐞𝐫𝐫𝐮𝐩𝐭 𝐛𝐮𝐭 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐛𝐞𝐟𝐨𝐫𝐞 𝐈 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮 𝐭𝐡𝐞 𝐟𝐢𝐥𝐞(𝐬).</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ᴡʜʏ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ ᴡɪʟʟ ʏᴏᴜ ꜱᴇɴᴅ ᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ?? ɪ'ᴍ ᴊᴜꜱᴛ ᴀ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ, ʙᴜᴅᴅʏ.\n\nᴜꜱᴇ @infohubrequest_robot ᴛᴏ ᴘʟᴀᴄᴇ ᴍᴏʀᴇ ʀᴇQᴜᴇꜱᴛꜱ."

ADMINS.append(OWNER_ID)
ADMINS.append(6011680723)

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
