from typing import List

from telegram import InlineKeyboardButton


class GreetingMessage:
    text: str = (
        "👋 **Hello! I'm your friendly Task Manager Bot!**\n"
        "I'm here to help you stay organized by creating lists, adding tasks,"
        " and customizing them just the way you like! 🎯📝\n\n"
        "✨ **Here are some commands you can use:**\n"
        "  **/start** – Display this welcome message 🌟\n"
        "  **/about** – Create a brand new list 📋\n"
        "  **/addlist** – Add a task to one of your lists ✅\n"
        "  **/customize** – Personalize your lists and tasks 🎨🔧\n"
    )
    buttons: List[str] = [
        InlineKeyboardButton("Create New List", callback_data="new_list"),
    ]
