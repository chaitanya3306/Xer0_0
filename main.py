from telegram.ext import ApplicationBuilder
from config import API_TOKEN
from handlers import commands,messages

app = ApplicationBuilder().token(API_TOKEN).build()

# Register all command handlers
app.add_handler(commands.start_handler)
app.add_handler(commands.help_handler)
app.add_handler(commands.menu_handler)
app.add_handler(commands.about_handler)
app.add_handler(commands.contact_handler)

# Register message handler for buttons/text
app.add_handler(messages.message_handler)

print("Bot started...")
app.run_polling()
