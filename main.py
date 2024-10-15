from app.services.bot_service import create_application
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:
    application = create_application()
    application.run_polling()


if __name__ == "__main__":
    main()
