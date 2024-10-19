import logging

from sqlalchemy.orm import Session
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ContextTypes,
)

from app.dependencies import get_db
from app.models import TaskList, Task
from app.services.buttons import get_add_task_button
from app.services.crud import get_task_list, create_task_list, create_task

logger = logging.getLogger(__name__)


async def user_task_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    db: Session = next(get_db())
    query = update.callback_query
    list_id = int(query.data.split("_")[1])

    task_list = await get_task_list(list_id, query, db)

    if task_list is None:
        return

    if not task_list.tasks:
        message = f'No tasks in "{task_list.name}" list yet.'
    else:
        message = f'Here are the tasks in "{task_list.name}" list:\n'
        message += "\n".join([f"• {task.title}" for task in task_list.tasks])

    add_task_button = get_add_task_button()
    reply_markup = InlineKeyboardMarkup([[add_task_button]])

    context.user_data["list_id"] = task_list.id
    await query.answer()
    await query.edit_message_text(text=message, reply_markup=reply_markup)


async def create_list_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text="Please send the name of the new list.")
    else:
        await update.message.reply_text(text="Please send the name of the new list.")

    context.user_data["awaiting_task_list_name"] = True


async def create_task_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Please send text of the new task:")

    context.user_data["awaiting_task_title"] = True


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get("awaiting_task_list_name"):
        db: Session = next(get_db())
        list_name = update.message.text
        username = update.message.from_user.username
        # reply_markup = []
        await create_task_list(list_name, username, update, context, db)
    elif context.user_data.get("awaiting_task_title"):
        db: Session = next(get_db())
        task_title = update.message.text
        list_id = context.user_data["list_id"]
        # reply_markup = []
        await create_task(list_id, task_title, update, context, db)
    else:
        await update.message.reply_text("I don't understand you ;(")
