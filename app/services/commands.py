from sqlalchemy.orm import Session
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.constants import ParseMode
from telegram.ext import (
    ContextTypes,
)

from app.const import GreetingMessage
from app.dependencies import get_db
from app.models import TaskList, Task
from app.services.buttons import get_task_list_buttons, get_add_task_list_button
from app.services.crud import get_task_lists_by_username


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    button = get_add_task_list_button()
    reply_markup = InlineKeyboardMarkup([[button]])

    await update.message.reply_text(
        GreetingMessage.text, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup
    )


async def user_task_lists_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    db: Session = next(get_db())
    username = update.message.from_user.username

    task_lists = get_task_lists_by_username(username, update, db)

    buttons = get_task_list_buttons(task_lists)
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "Here are your task lists:", reply_markup=reply_markup
    )
