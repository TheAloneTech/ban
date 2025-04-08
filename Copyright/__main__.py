import logging
import asyncio
import importlib

from pyrogram import idle
from Copyright import app
from Copyright.plugins import ALL_MODULES

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Silence some logs
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

log = logging.getLogger("Copyright-Community-Bot")

async def main():
    log.info("Starting bot...")
    await app.start()

    # Import all modules
    for module_name in ALL_MODULES:
        try:
            importlib.import_module(f"Copyright.{module_name}")
            log.info(f"Loaded module: {module_name}")
        except Exception as e:
            log.error(f"Failed to load module {module_name}: {e}")

    log.info("Bot Started Successfully!")
    await idle()
    log.info("Bot Stopped. Shutting down...")
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
