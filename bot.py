from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello, World!')

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    application = Application.builder().token("8136796501:AAHniJ9Y9B3MQLiEcawEFj6RAZ6Akjmk9iA").build()
    
    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))
    
    # Run the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
