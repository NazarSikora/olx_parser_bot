# OLX Parser Bot

A Telegram bot for monitoring OLX listings prices built with Python and aiogram 3.x.

## Features

- Add OLX listings by URL for monitoring
- View all saved listings
- Check actual prices on demand
- Detect price changes automatically
- Delete listings from your watchlist

## Tech Stack

- **aiogram 3.x** — async Telegram bot framework
- **httpx** — async HTTP client for fetching pages
- **BeautifulSoup4** — HTML parsing
- **aiosqlite** — async SQLite database
- **python-dotenv** — environment variables management

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/your_username/olx-parser-bot.git
cd olx-parser-bot
```

**2. Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file**
```
BOT_TOKEN=your_telegram_bot_token
```

**5. Run the bot**
```bash
python bot.py
```

## Usage

| Command | Description |
|---|---|
| `/start` | Show welcome message and commands |
| `/add <url>` | Add OLX listing to watchlist |
| `/list` | Show all saved listings |
| `/get` | Fetch actual prices for all listings |
| `/delete <id>` | Remove listing from watchlist |

## Example
```
/add https://www.olx.ua/uk/obyavlenie/...

✅ Saved!
📦 Apple iPhone 15 Pro Max
💰 33 000 UAH.
```

## Notes

> OLX uses dynamic CSS classes that may change after site updates.
> If parsing stops working — inspect the listing page and update class names in `parser/olx.py`.