from telegram.ext import MessageHandler, filters, ContextTypes
from telegram import Update,ReplyKeyboardMarkup, KeyboardButton

async def handle_user_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    if user_input == "🧑‍💻 Programming":
        keyboard = [
        [KeyboardButton("⌨️ What is Programming")],
        [KeyboardButton("🐍 Python")],
        [KeyboardButton("🖥 C++")],
        [KeyboardButton("☕ Java")], 
        [KeyboardButton("🌐 JavaScript")],
        
        [KeyboardButton("⬅️ Back to Menu")]
        
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

        await update.message.reply_text(
            "Choose a programming language:",
            reply_markup=reply_markup
        )
        
    elif user_input == "🎯 Career Roadmaps":
        await update.message.reply_text("Choose a field:\n• Data Science\n• Web Development\n• App Development")

    elif user_input == "📰 Tech News":
        await update.message.reply_text("Fetching top tech news... 🔄 (will integrate API soon!)")

    elif user_input == "📞 Contact Us":
        # You can call the contact function here if imported, or just reply
        await update.message.reply_text("You can contact @YourTelegramUsername anytime!")

    elif user_input == "ℹ️ About":
        await update.message.reply_text("This is Skillub Bot! A place for learning and tech updates.")

    else:
        await update.message.reply_text("Please choose a valid option from the menu.")

message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user_selection)
