import logging
import asyncio
import importlib

from pyrogram import Client, idle
from Copyright import config
from Copyright.plugins import ALL_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger("Copyright-Community-Bot")

app = Client(
    name="bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

async def main():
    log.info("Starting bot...")

    await app.start()

    for module in ALL_MODULES:
        try:
            importlib.import_module(f"Copyright.plugins{module}")
        except Exception as e:
            log.error(f"Failed to import {module}: {e}")

    log.info("Bot Started.")
    await idle()
    await app.stop()
    log.info("Bot Stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("Bot stopped manually.")
