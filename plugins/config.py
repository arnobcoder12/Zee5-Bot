import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5152148642:AAFuZsIo6urDBVByCIQDHoFwEbYD5STsHYU")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 16151559))
    API_HASH = os.environ.get("API_HASH", "1a43ce7c13c0fc46871f9220ff9778f0")
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
 
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "756439645"))
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "xurluploader")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://lcgvofqddigjrn:d89ee54807c63034d72b13c3fad9422399820d473233002531c21bfe6da01f3d@ec2-3-225-79-57.compute-1.amazonaws.com:5432/d5gan7cid74654
")
    
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
