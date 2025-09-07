import logging
from pyrogram import Client
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Debug print to check config values
print("BOT_TOKEN =", Config.BOT_TOKEN)
print("API_ID =", Config.API_ID)
print("API_HASH =", Config.API_HASH)

class autocaption(Client):
    def __init__(self):
        super().__init__(
            session_name="Captioner",                    # Correct argument for session name
            bot_token=Config.BOT_TOKEN,          # Bot token from config
            api_id=Config.API_ID,                # API ID from config
            api_hash=Config.API_HASH,            # API Hash from config
            workers=20,
            plugins=dict(root="Plugins")         # Plugins directory
        )

if __name__ == "__main__":
    autocaption().run()
