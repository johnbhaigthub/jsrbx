# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27161113"))
API_HASH = getenv("API_HASH", "65c4b51f54049ebe22bc01fd9a95975b")
BOT_TOKEN = getenv("BOT_TOKEN", "8058972609:AAE7TwlqxpME8FxnbvJoD4K7BWMqe3-H4vU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6401497985").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://khatrirajesh1003:P8TK8d121m5a0a4k@rajesh01.niiho.mongodb.net/?retryWrites=true&w=majority&appName=rajesh01")
LOG_GROUP = getenv("LOG_GROUP", "-1002366201837")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002374060756"))
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002374060756"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "")
