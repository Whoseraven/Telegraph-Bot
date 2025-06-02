import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyrogram client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config get this from mongodb
    DB_NAME = os.environ.get("DB_NAME","sumitsajwan135")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/06923cc70e2ecedcb2c8d-dd1ffb11c5eab68b07.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7577853954').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Kirito_Bots")
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002468277277'))

    # download file
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
    
class Txt(object):

    START_TXT = """<b>ʜᴇʏ, {}
    
I ᴀᴍ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ʙᴏᴛ. sᴇɴᴅ ᴍᴇ ɪᴍᴀɢᴇ, ɢɪғs ᴀɴᴅ ᴠɪᴅᴇᴏs ᴀɴᴅ I ᴡɪʟʟ ᴘʀᴇᴘᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ɢɪᴠᴇ ɪᴛ ᴛᴏ ʏᴏᴜ.
 </b>"""

    ABOUT_TXT = """<b>➤ Mʏ Nᴀᴍᴇ: {}
➤ Cʀᴇᴀᴛᴏʀ : <a href='tg://settings'>Tʜɪs Pᴇʀsᴏɴ</a>
➤ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/whosekirito'>Rᴋɴ Dᴇᴠᴇʟᴏᴘᴇʀ</a>
➤ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
➤ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
➤ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
➤ Bᴏᴛ Sᴇʀᴠᴇʀ : ʀᴇɴᴅᴇʀ
➤ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ1.0.1</b> """
    
    
    HELP_TXT = """
🌌 <b><u>HOW TO USE THIS BOT</u></b>
  
• ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ ɪᴍᴀɢᴇ, ɢɪғs ᴀɴᴅ ᴠɪᴅᴇᴏs.
• ɪ ᴡɪʟʟ ᴘʀᴇᴘᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ɢɪᴠᴇ ɪᴛ ᴛᴏ ʏᴏᴜ.
• ғɪʟᴇ sᴜᴘᴘᴏʀᴛ ᴍᴀxɪᴍᴜᴍ ғɪʟᴇ sɪᴢᴇ ʟɪᴍɪᴛ ɪs 𝟻ᴍʙ.
"""
