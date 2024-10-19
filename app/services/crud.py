from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import ContextTypes

from app.models import TaskList, Task


def get_task_lists_by_username(username: int, update: Update, db: Session):
    if not username:
        return update.message.reply_text("You should make your username not private.")

    lists = db.query(TaskList).filter(TaskList.username == username).all()

    if not lists:
        return update.message.reply_text("You don't have any task lists yet.")
    return lists


async def get_task_list(list_id: int, update: Update, db: Session) -> TaskList | None:
    task_list = db.query(TaskList).get(list_id)

    if task_list is None:
        await update.message.reply_text("Some error occurred.")
        return None

    return task_list


def create_task_list(
    list_name: str,
    username: str,
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    db: Session,
    reply_markup: list | None = None,
):
    try:
        new_task_list = TaskList(name=list_name, username=username)
        db.add(new_task_list)
        db.commit()
        db.flush()

        return update.message.reply_text(
            f'List "{list_name}" created successfully!', reply_markup=reply_markup
        )
    except Exception:
        db.rollback()
        return update.message.reply_text(
            "Some error occurred while creation of task list."
        )
    finally:
        context.user_data["awaiting_task_list_name"] = False


def create_task(
    list_id: int,
    task_title: str,
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    db: Session,
    reply_markup: list | None = None,
):
    try:
        new_task = Task(title=task_title, list_id=list_id)
        db.add(new_task)
        db.commit()
        db.flush()
        return update.message.reply_text(
            f'Task "{new_task.title}" created successfully!',
            reply_markup=reply_markup,
        )
    except Exception:
        db.rollback()
        return update.message.reply_text("Some error occurred while creation of task.")
    finally:
        del context.user_data["list_id"]
        context.user_data["awaiting_task_title"] = False
