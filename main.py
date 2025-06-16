import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Конфигурация
BOT_TOKEN = "7825085787:AAHWd3242SETfxt5iGW-7vfcnl5mrVbxwOQ"  # Ваш токен
WEB_APP_URL = "https://sergei00777.github.io/miniAPPS/" # URL вашего Mini App


# Обработчик команды /start
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Открыть Mini App", web_app={"url": WEB_APP_URL})]
    ]
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть Mini App:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Обработчик для любых сообщений
async def handle_message(update: Update, context):
    await update.message.reply_text("Напишите /start для запуска Mini App.")


# Настройка и запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()