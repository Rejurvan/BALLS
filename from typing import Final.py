from typing import Final

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

BOT_TOKEN: Final = "6659704559:AAHBMlYsubg3rQ_DBxGD15YfFLzTONC514A"


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello, I'm a bot! Thanks for using me!",
        reply_to_message_id=update.effective_message.id,
    )


async def upper_case_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # write your code here
    pass


async def echo_sticker_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    # write your code here
    pass


if __name__ == "__main__":
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # adding handlers
    bot.add_handler(CommandHandler("start", start_command_handler))
    bot.add_handler(MessageHandler(filters.TEXT, upper_case_message_handler))
    bot.add_handler(MessageHandler(filters.Sticker.ALL & filters.Sticker.VIDEO & filters.Sticker.STATIC, echo_sticker_message_handler))
    # add all your handlers here
    # start bot
    bot.run_polling()
