import enum


class GreetingMessage:
    text: str = (
        "👋 **Hello! I'm your friendly Task Manager Bot!**\n"
        "I'm here to help you stay organized by creating lists, adding tasks,"
        " and customizing them just the way you like! 🎯📝\n\n"
        "✨ **Here are some commands you can use:**\n"
        "  /start – Display this welcome message 🌟\n"
        "  /mylists – Show all your lists ✅\n"
        "  /addlist – Create a new list 📋\n"
        "  /customize – Personalize your lists and tasks 🎨🔧 (does not work)\n"
    )


class TaskPriority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
