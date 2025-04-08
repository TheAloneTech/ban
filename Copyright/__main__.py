from pyrogram import Client
import config
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="[%d-%m-%Y %H:%M:%S]",
)
logger = logging.getLogger("Copyright-Community-Bot")

app = Client(
    name="copyright-bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins={"root": "Copyright/plugins"}
)

if __name__ == "__main__":
    logger.info("Starting bot...")
    app.run()
