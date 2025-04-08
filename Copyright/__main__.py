import logging
import asyncio
import importlib

from pyrogram import idle

from Copyright import app
from Copyright.plungins import ALL_MODULES

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]  # Output to console
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

log = logging.getLogger("Copyright-Community-Bot")

async def main():
    log.info("Starting bot...")
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module("Copyright.plungins" + all_module)
    log.info("Bot Started")
    await idle()
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
