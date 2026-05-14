import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from deep_translator import GoogleTranslator

# Bot tokenini shu yerga yozing
TOKEN = '8140307917:AAFxQjLyy53GBWRVjh0dtv4OlQan3rzroqE'
bot = telebot.TeleBot(TOKEN)

# /start buyrug'i bosilganda
@bot.message_handler(commands=['start'])
def send_welcome(message):
    xabar = "Salom! Menga biror matn yuboring, men esa uni tarjima qilib beraman."
    bot.reply_to(message, xabar)

# Oddiy matn kelganda faqat tugmalarni ko'rsatish
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    markup = InlineKeyboardMarkup()
    btn_en = InlineKeyboardButton("🇬🇧 Inglizchaga tarjima qilish", callback_data='to_en')
    btn_uz = InlineKeyboardButton("🇺🇿 O'zbekchaga tarjima qilish", callback_data='to_uz')
    
    markup.add(btn_en)
    markup.add(btn_uz)
    
    bot.reply_to(message, "Tarjima qilish uchun quyidagi tugmalardan birini bosing👇", reply_markup=markup)

# Tugma bosilganda tarjimani amalga oshirish
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Asl yozilgan matnni olish
    original_text = call.message.reply_to_message.text
    
    try:
        if call.data == 'to_en':
            # Matn tilini avtomatik aniqlab, inglizchaga tarjima qilish
            translated = GoogleTranslator(source='auto', target='en').translate(original_text)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                                  text=f"🇬🇧 Inglizcha tarjimasi:\n\n{translated}")
            
        elif call.data == 'to_uz':
            # Matn tilini avtomatik aniqlab, o'zbekchaga tarjima qilish
            translated = GoogleTranslator(source='auto', target='uz').translate(original_text)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                                  text=f"🇺🇿 O'zbekcha tarjimasi:\n\n{translated}")
            
    except Exception as e:
        bot.answer_callback_query(call.id, "Kechirasiz, tarjima qilishda xatolik yuz berdi!")

# Botni uzluksiz ishga tushirish
print("Yangi tarjimon bilan bot ishga tushdi...")
bot.infinity_polling()