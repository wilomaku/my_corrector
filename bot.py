import os
import requests

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """
You are a friendly English tutor.

Correct the user's English naturally.

Rules:
- Keep original meaning
- Be encouraging
- Give short explanations
- Do not over-correct
- Format clearly

Response format:

Corrected:
...

Notes:
- ...
"""

def correct_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        "temperature": 0.3,
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Use /correct as a reply to a message."
    )


async def correct(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if not message.reply_to_message:
        await message.reply_text(
            "Reply to a message with /correct"
        )
        return

    original_text = message.reply_to_message.text

    if not original_text:
        await message.reply_text(
            "I can only correct text messages."
        )
        return

    await message.reply_text("Correcting...")

    try:
        corrected = correct_text(original_text)
        await message.reply_text(corrected)

    except Exception as e:
        await message.reply_text(f"Error: {e}")


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("correct", correct))

print("Bot running...")

app.run_polling()
