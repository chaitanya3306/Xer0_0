# from config import API_TOCKEN
import telebot
from telegram.ext import *

app=ApplicationBuilder().token('8055457746:AAHp1RKAVDQRbWItJePiR3pm6dzR0_VaPnY'
).build()

async def start(update,context):
    await update.message.reply_text("hello welcome to XeroBot 👋")
    
start_handler=CommandHandler("start",start)
app.add_handler(start_handler)

# messageHandler

async def reply_text(update,context):
    await update.message.reply_text("Replied",reply_to_message_id=update.message.message_id)
    
text_handler=MessageHandler(filters.ALL & ~filters.COMMAND,reply_text)
app.add_handler(text_handler)

app.run_polling()