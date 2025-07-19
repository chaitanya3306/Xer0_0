from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes
#Start Command 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🧑‍💻 Programming")], 
        [KeyboardButton("🎯 Career Roadmaps")],
        [KeyboardButton("📰 Tech News")],
        [KeyboardButton("🤖 AI Tools")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Hello! Welcome to *Skillub Bot*.\n\n"
        "Please choose an option below to get started:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    
# help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(help_text, parse_mode="Markdown")
    
# menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📞 Contact Us")],
        [KeyboardButton("🤖 All AI Tools")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "📋 *Choose an option below:*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# About
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text(about_text, parse_mode='Markdown')
    
# contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_text = (
        "📬 *Got a suggestion or need help?*\n"
        "You can reach out to the developer directly!\n\n"
        "🧑‍💻 *Created by:* @YourTelegramUsername\n"
        "📩 Feel free to send feedback or ideas!"
    )
    keyboard = [
        [InlineKeyboardButton("📨 Message Developer", url="https://t.me/Chaitanya")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(contact_text, parse_mode="Markdown", reply_markup=reply_markup)

# Register handlers for commands
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
menu_handler = CommandHandler("menu", menu)
about_handler = CommandHandler("about", about)
contact_handler = CommandHandler("contact", contact)
