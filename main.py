import os
import logging
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
)

from app.base import Base, engine
from app.services.bot_service import (
    echo,
    user_task_list,
    create_list_callback,
    create_task_callback,
)
from app.services.commands import start_command, user_task_lists_command


load_dotenv()

TOKEN = os.getenv("TG_BOT_TOKEN")

Base.metadata.create_all(engine)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def create_application() -> Application:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("mylists", user_task_lists_command))
    application.add_handler(CommandHandler("addlist", create_list_callback))
    application.add_handler(
        CallbackQueryHandler(create_list_callback, pattern="create_list")
    )
    application.add_handler(
        CallbackQueryHandler(create_task_callback, pattern="create_task")
    )
    application.add_handler(CallbackQueryHandler(user_task_list, pattern="list_"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    return application


def main() -> None:
    application = create_application()
    application.run_polling()


if __name__ == "__main__":
    main()
