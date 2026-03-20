import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'api', '.env'))

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# RunPod configuration from environment
API_URL = os.getenv("RUNPOD_CHATBOT_URL")
API_KEY = os.getenv("RUNPOD_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")
if not API_KEY:
    raise ValueError("RUNPOD_TOKEN not found in environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("☕ Coffee AI Bot Ready! Use /ask to chat.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /ask <your question>")

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("Please provide a query. Example: /ask I want a strong coffee")
        return

    try:
        # Format message as expected by the agent controller
        messages = [{"content": query, "role": "user"}]

        response = requests.post(
            API_URL,
            json={"input": {"messages": messages}},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            }
        )

        response_data = response.json()
        # Extract the response from the output
        reply = response_data.get("output", {}).get("content", "No response from AI")

        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text(f"Error connecting to AI system: {str(e)}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ask", ask))

app.run_polling()
