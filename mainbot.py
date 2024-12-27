from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

YANDEX_API_KEY = 'your_yandex_translate_api_key'
YANDEX_API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

target_languages = {}

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    target_languages[user.id] = 'en'
    update.message.reply_text(
        f"Привет, {user.first_name}! Я бот для перевода текста.\n"
        "Отправь мне текст для перевода, и я переведу его на английский.\n"
        "Используй /setlang, чтобы выбрать целевой язык."
    )

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Я бот для перевода текста. Вот что я могу:\n"
        "- Отправь мне текст, и я переведу его на выбранный язык.\n"
        "- Используй /setlang, чтобы изменить целевой язык.\n"
        "Поддерживаемые языки: en (английский), ru (русский), es (испанский), и другие."
    )

def set_language(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    if context.args:
        lang = context.args[0]
        target_languages[user.id] = lang
        update.message.reply_text(f"Целевой язык установлен: {lang}")
    else:
        update.message.reply_text("Пожалуйста, укажите язык. Например: /setlang en")

def translate_text(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    text_to_translate = update.message.text
    target_language = target_languages.get(user.id, 'en')
    params = {'key': YANDEX_API_KEY, 'text': text_to_translate, 'lang': target_language}
    response = requests.get(YANDEX_API_URL, params=params)
    data = response.json()

    if response.status_code == 200 and 'text' in data:
        translated_text = data['text'][0]
        update.message.reply_text(f"Перевод ({target_language}): {translated_text}")
    else:
        update.message.reply_text("Произошла ошибка при переводе текста. Попробуйте позже.")

def main() -> None:
    TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("setlang", set_language))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
