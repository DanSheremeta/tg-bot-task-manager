from telegram import (
    Update,
    InlineKeyboardMarkup,
)
from telegram.constants import ParseMode
from telegram.ext import (
    ContextTypes,
)

from app.const import GreetingMessage


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = InlineKeyboardMarkup([GreetingMessage.buttons])

    await update.message.reply_text(
        GreetingMessage.text, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)
