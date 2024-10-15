# Telegram Bot

This is a simple Telegram bot built using the `python-telegram-bot` library.

## Prerequisites

- Python 3.7+
- `pip` (Python package installer)

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory and add your Telegram bot token:
    ```dotenv
    TG_BOT_TOKEN=your_actual_token_here
    ```

## Running the Bot

1. **Run the bot**:
    ```sh
    python main.py
    ```

## Project Structure

- `main.py`: Entry point to run the bot.
- `app/services/bot_service.py`: Contains the bot logic and handlers.
- `.env`: Environment file containing the bot token.
