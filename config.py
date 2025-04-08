from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "28795512"))
API_HASH = getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a")

BOT_TOKEN = getenv("BOT_TOKEN", "7239027308:AAEBqtklQD_K-jYkahMI-hUaMiEOvR3Tw40")

OWNER_ID = int(getenv("OWNER_ID", "7879180190"))

MONGO_DB_URI = getenv("MONGO_URL", "mongodb+srv://Radheee:sanatani@cluster0.sgop4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OTHER_LOGS = int(getenv("OTHER_LOGS", "-1002644496954"))
LOGGER_ID  = int(getenv("LOGGER_ID", "-1002664280831"))
