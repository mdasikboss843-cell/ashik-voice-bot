import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হাই! আমি চালু আছি ✅")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ভয়েস পেয়েছি ভাই ❤️")

if __name__ == '__main__':
    import asyncio
    async def main():
        if not BOT_TOKEN:
            print("BOT_TOKEN পাওয়া যায়নি!")
            return
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.VOICE, handle_voice))
        print("Bot is running...")
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        await asyncio.Event().wait()
    asyncio.run(main())
