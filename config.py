# REQUIRED CONFIG
BOT_TOKEN = ""
OWNER_ID = 0
TELEGRAM_API = 0
TELEGRAM_HASH = ""
DATABASE_URL = ""

# OPTIONAL CONFIG
DEFAULT_LANG = "en"
TG_PROXY = (
    {}
)  # {"scheme": ”socks5”, "hostname": ””, "port": 1234, "username": ”user”, "password": ”pass”}
USER_SESSION_STRING = "BQFDFIQARjmJejOMA-ukpSF0TYJxQKahDUjjHoECeScl9hY13ORb38V93iskslMEpwjhYRc7wqbryE8Z4n6ZX-eH4ChQv68EwezNdRj8qw3fCiZItTyBYd1GnMMlz10qda8I5VOz7dA2sUOKJFLWP7sdhqEjl1baE0JPrtZxttRXITvgG2sNOrsGaYmBYe8ZQ3bS2YuTmfzm6qekXO5HdIJ9l-RPL8laAts6h65KBeSyUogDVurRBpPzIZdmxflBpF3YdPO0x7zCksdnLxeRXIatF4ceTm-XqCdpKw8OhPAomPgFAtAK6g6M4U5c-M213t_SgamGSvgcWSJ-R40h-JDZBW0pPgAAAAHWiyDOAA                   "
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
STATUS_LIMIT = 10
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SWAP = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}

# Custom Bot Header
CUSTOM_BOT_HEADER = "Beast"
CUSTOM_BOT_HEADER_LINK = "https://t.me/MirrorBeast"

# Hyper Tg Downloader
HELPER_TOKENS = ""

# MegaAPI v4.30
MEGA_EMAIL = ""
MEGA_PASSWORD = ""

# Disable Options
DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False

# Telegraph
AUTHOR_NAME = "Beast"
AUTHOR_URL = "https://t.me/MirrorBeast"

# Task Limits
DIRECT_LIMIT = 100
MEGA_LIMIT = 10 
TORRENT_LIMIT = 100
GD_DL_LIMIT = 100
RC_DL_LIMIT = 100
CLONE_LIMIT = 20
JD_LIMIT = 23
YTDLP_LIMIT = 50
PLAYLIST_LIMIT = 60
LEECH_LIMIT = 50
EXTRACT_LIMIT = 40
ARCHIVE_LIMIT = 40
STORAGE_LIMIT = 100

# Insta video downloader api
INSTADL_API = ""

# Media Search
IMDB_TEMPLATE = """<b>🎬 Title:</b> <a href="{url}">{title}</a> <b>({year})</b>
<b>🎭 Also Known As:</b> <i>{aka}</i>
<b>⭐ Rating:</b> <i>{rating}/10</i>
<b>📅 Release Date:</b> <a href="{url_releaseinfo}">{release_date}</a>
<b>📚 Genre:</b> {genres}
<b>🗣️ Language:</b> {languages}
<b>🌍 Country:</b> {countries}

<b>📖 Storyline:</b>
<code>{plot}</code>

<b>🔗 Explore More:</b> <a href="{url_cast}">Full Cast & Details</a> | <a href="{url}">IMDb Page</a>"""

# Task Tools
FORCE_SUB_IDS = ""
MEDIA_STORE = True
DELETE_LINKS = False
CLEAN_LOG_MSG = False

# Limiters
BOT_MAX_TASKS = 20
USER_MAX_TASKS = 3
USER_TIME_INTERVAL = 10
VERIFY_TIMEOUT = 100
LOGIN_PASS = ""

# Bot Settings
BOT_PM = False
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded by Beast"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""
SHOW_CLOUD_LINK = False

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Update
UPSTREAM_REPO = "https://github.com/MokeyDLuf88/ABML-X.git"
UPSTREAM_BRANCH = "master"
UPDATE_PKGS = True

# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
USER_TRANSMISSION = True
HYBRID_LEECH = True
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""

# Log Channels
LEECH_DUMP_CHAT = "-1002964190861"
LINKS_LOG_ID = "-1002964190861"
MIRROR_LOG_ID = "-1002964190861"

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
BASE_URL_PORT = 0
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 5
QUEUE_DOWNLOAD = 3
QUEUE_UPLOAD = 3

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
