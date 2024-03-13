from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a75fdf21d307b98b6f632.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/34ff76a850f28c2d39ca9.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/P_PP_Pi")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/P_PP_Pi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6396782078").split()))


FAILED = "https://telegra.ph/file/5f52312e9021cd9268077.jpg"
