import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from deep_translator import GoogleTranslator
from flask import Flask
from threading import Thread

TOKEN = "8605982220:AAHnqKLA6sCxdh4SGAXpu7F1aa6z9LWHGYU"
bot = telebot.TeleBot(TOKEN)

# Flask server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 10000))
    )

def keep_alive():
    t = Thread(target=run)
    t.start()

# /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    xabar = "Salom! Menga biror matn yuboring, men esa uni tarjima qilib beraman."
    bot.reply_to(message, xabar)

# Matn kelganda
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    markup = InlineKeyboardMarkup()

    btn_en = InlineKeyboardButton(
        "🇬🇧 Inglizchaga tarjima qilish",
        callback_data='to_en'
    )

    btn_uz = InlineKeyboardButton(
        "🇺🇿 O'zbekchaga tarjima qilish",
        callback_data='to_uz'
    )

    markup.add(btn_en)
    markup.add(btn_uz)

    bot.reply_to(
        message,
        "Tarjima qilish uchun tugmani bosing👇",
        reply_markup=markup
    )

# Tugma bosilganda
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    try:
        original_text = call.message.reply_to_message.text

        if call.data == 'to_en':

            translated = GoogleTranslator(
                source='auto',
                target='en'
            ).translate(original_text)

            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"🇬🇧 Inglizcha tarjimasi:\n\n{translated}"
            )

        elif call.data == 'to_uz':

            translated = GoogleTranslator(
                source='auto',
                target='uz'
            ).translate(original_text)

            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=f"🇺🇿 O'zbekcha tarjimasi:\n\n{translated}"
            )

    except Exception as e:
        print(e)

        bot.answer_callback_query(
            call.id,
            "Tarjima qilishda xatolik yuz berdi!"
        )

# Flask serverni ishga tushirish
keep_alive()

print("Bot ishga tushdi...")

# Bot polling
bot.infinity_polling(skip_pending=True)