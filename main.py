import os
import logging
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from app.services.bot_service import start, echo

load_dotenv()

TOKEN = os.getenv("TG_BOT_TOKEN")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def create_application() -> Application:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler(start.__name__, start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    return application


def main() -> None:
    application = create_application()
    application.run_polling()


if __name__ == "__main__":
    main()
