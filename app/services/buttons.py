from telegram import InlineKeyboardButton


def get_add_task_button() -> InlineKeyboardButton:
    return InlineKeyboardButton("Add new task", callback_data=f"create_task")


def get_add_task_list_button() -> InlineKeyboardButton:
    return InlineKeyboardButton("Create New List", callback_data="create_list")


def get_task_list_buttons(lists: list) -> list:
    return [
        [InlineKeyboardButton(task_list.name, callback_data=f"list_{task_list.id}")]
        for task_list in lists
    ]
