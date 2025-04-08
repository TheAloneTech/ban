import logging
import asyncio
import importlib

from pyrogram import idle
from Copyright import app
from Copyright.plugins import ALL_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

log = logging.getLogger("Copyright-Community-Bot")


async def main():
    log.info("Starting bot...")
    await app.start()

    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"Copyright.plungins{all_module}")
        except Exception as e:
            log.error(f"Failed to import {all_module}: {e}")

    log.info("Bot Started")
    await idle()
    await app.stop()
    log.info("Bot Stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())  # ✅ safest way to handle event loop
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot stopped by user.")
