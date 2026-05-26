from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

# App Database
apps = {
    "inshot": "https://t.me/c/2576380290/400"
}

# Auto Reply System
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    for app in apps:
        if app in text:

            # Download Button
            button = [
                [InlineKeyboardButton(
                    "⬇️ Download App",
                    url=apps[app]
                )]
            ]

            keyboard = InlineKeyboardMarkup(button)

            # Premium Message
            message = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 App Name : {app.title()}

🔗 Download Link Ready
⚡ Powered By : ModxStore
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message,
                reply_markup=keyboard
            )

            break


# Bot Setup
app = ApplicationBuilder().token("8399577225:AAER76rIxXT3SDTiw-dfHQT8bezSuhqxcMw").build()

# Message Handler
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
)

print("🚀 Premium Bot Running...")

app.run_polling(
    drop_pending_updates=True,
    close_loop=False
)