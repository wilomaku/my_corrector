# English Study Bot

A simple Telegram bot for English practice groups.

Users can write messages in English and invoke the bot with `/correct` to receive friendly grammar and vocabulary corrections powered by a free LLM API.

## Features

- Telegram group integration
- English correction on demand
- Friendly explanations
- Free LLM inference using Groq
- Lightweight Python implementation

## Example

User message:

> I have went to the supermarket yesterday.

Reply with:

```text
/correct
```

Bot response:

> Corrected:
> I went to the supermarket yesterday.
>
> Notes:
> - "have went" → "went" (correct past tense)

## Stack

- Python
- python-telegram-bot
- Groq API
- Telegram Bot API

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd english-study-bot
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

Linux/macOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```env
TELEGRAM_BOT_TOKEN=your_token
GROQ_API_KEY=your_key
```

### 5. Run the bot

```bash
python bot.py
```

## Telegram Setup

1. Create a bot with `@BotFather`
2. Add the bot to your group
3. Disable privacy mode with:

```text
/setprivacy
```

4. Promote the bot to admin
