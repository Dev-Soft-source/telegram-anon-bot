# Telegram Anonymous Bot

A Python Telegram bot built with [aiogram](https://docs.aiogram.dev/) that registers users in a database and is intended to relay private messages to a channel under the bot’s identity so they appear anonymous to channel readers. The core relay and persistence logic is present in the data model but currently commented out in the message handler; the bot still responds that a message was posted, which is useful while wiring up the channel and permissions.

## Features

- **`/start`** — Creates or updates a user record (Telegram user id, username) and shows whether the user is treated as an admin.
- **Admin detection** — User ids listed in `ADMIN_IDS` are marked as admins in the database and in the welcome text.
- **Database** — Async SQLAlchemy with SQLite by default (`users` and `comments` tables). `Comment` is meant to map a user to a channel message id once relay is enabled.

## Requirements

- Python 3.10+ (recommended)
- Dependencies are listed in `requirements.txt` (aiogram 3.x, SQLAlchemy 2 async, aiosqlite, python-dotenv).

## Setup

1. Clone or copy this repository and create a virtual environment:

   ```bash
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root (same folder as `requirements.txt`) with:

   | Variable | Required | Description |
   |----------|----------|-------------|
   | `BOT_TOKEN` | Yes | Token from [@BotFather](https://t.me/BotFather). |
   | `CHANNEL_ID` | Yes | Target channel id (e.g. `-1001234567890`). The bot must be an administrator in that channel to post. |
   | `ADMIN_IDS` | No | Comma-separated Telegram user ids of admins (e.g. `123456789,987654321`). |
   | `DATABASE_URL` | No | Default: `sqlite+aiosqlite:///./bot.db` |

3. Run the bot from the project root:

   ```bash
   python -m src.main
   ```

   Ensure your working directory is the repository root so the SQLite file path and imports resolve as expected.

## Project layout

| Path | Role |
|------|------|
| `src/main.py` | Application entry: creates database tables and starts polling. |
| `src/config.py` | Loads environment variables and constructs the `Bot` instance. |
| `src/handlers.py` | Command and message handlers (`/start`, anonymous flow). |
| `src/database.py` | Async engine and session factory. |
| `src/models.py` | SQLAlchemy models: `User`, `Comment`. |

## Enabling anonymous relay

To actually forward private text to the channel and store `Comment` rows, uncomment and adjust the block in `anonymous_post` in `src/handlers.py`, and remove or replace the placeholder reply. You may also want to restrict handling to private chats only (`message.chat.type == "private"`) so group messages are not forwarded by mistake.

## License

Add a license file if you distribute this project.
