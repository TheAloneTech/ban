import logging
import asyncio
import importlib
from config import *
from pyrogram import Client, idle
from Copyright.plugins import ALL_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

log = logging.getLogger("Copyright-Community-Bot")

# ✅ yahan par hi app define karte hain
app = Client(
    name="copyright_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def main():
    log.info("Starting bot...")
    await app.start()

    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"Copyright.plugins{all_module}")
        except Exception as e:
            log.error(f"Failed to import {all_module}: {e}")

    log.info("Bot Started")
    await idle()
    await app.stop()
    log.info("Bot Stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot stopped by user.")
