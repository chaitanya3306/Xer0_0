from config import API_TOCKEN
from telegram.ext import *
from telegram import *

app=ApplicationBuilder().token(API_TOCKEN).build()

# Commands

# start command function
async def start(update,context):
    await update.message.reply_text("hello welcome to Xer0_0.Bot 👋")
# help command function
async def help(update, context):
    help_text = (
        "👋 *Welcome to SkillubBot!*\n\n"
        "Here’s what I can help you with:\n\n"
        "🔹 *Explore Programming Languages*\n"
        "🔹 *Follow Career Roadmaps* (Data Science, Web Dev, ML, etc.)\n"
        "🔹 *Get Daily Tech News*\n\n"
        "Type /menu to start using the bot or use the buttons provided.\n\n"
        "ℹ️ *Commands:*\n"
        "/start --> Restart the bot\n"
        "/help  --> Show this help menu\n"
        "/menu  --> Show main menu again\n"
        "/about --> Know about this bot\n\n"
        "🔗 Contact @Chaitanya for feedback or support!"
    ) 
    await update.message.reply_text(help_text,parse_mode="Markdown")

# menu command function 
async def menu(update,context):
    keyboard = [
        [KeyboardButton("🧑‍💻 Programming Languages")],
        [KeyboardButton("🎯 Career Roadmaps")],
        [KeyboardButton("📰 Tech News")],
        [KeyboardButton("📞 Contact Us")],
        [KeyboardButton("🤖 All AI Tools ")]
    ]
    reply_markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)
    
    await update.message.reply_text(
         "📋 *Choose an option below:*",
         reply_markup=reply_markup,
         parse_mode="Markdown"
    )

#about command function
async def about(update,context):
    
    about_text = (
    "👋 *Welcome to Xer0_0.Bot!*\n\n"
    "📚 This bot is designed for *students, tech enthusiasts,* and *learners* who want:\n"
    "• 📘 Programming resources\n"
    "• 🎯 Career roadmaps in tech\n"
    "• 📰 Daily tech news\n"
    "• 💬 A growing community space\n"
    "• 🔍 All AI Tools\n\n\n"
    "💡 *Built with 💖 by a student for students!*"
     )
    await update.message.reply_text(about_text,parse_mode='Markdown')
        
# contact command function

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_text = (
        "📬 *Got a suggestion or need help?*\n"
        "You can reach out to the developer directly!\n\n"
        "🧑‍💻 *Created by:* @YourTelegramUsername\n"
        "📩 Feel free to send feedback or ideas!"
    )

    # Optional: Add a button to contact directly
    keyboard = [
        [InlineKeyboardButton("📨 Message Developer", url="https://t.me/Chaitanya")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(contact_text, parse_mode="Markdown", reply_markup=reply_markup)

# all command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("menu",menu))
app.add_handler(CommandHandler("about",about))

# messageHandler

async def reply_text(update,context):
    await update.message.reply_text("Replied",reply_to_message_id=update.message.message_id)
    
text_handler=MessageHandler(filters.TEXT & ~filters.COMMAND,reply_text)
app.add_handler(text_handler)

app.run_polling()
