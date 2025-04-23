import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Ton token Telegram ici
BOT_TOKEN = "7115175533:AAHcFYSUzqagDMuxOttx4jLUNCDdlVyvtZo"
SUPPORT_USERNAME = "blackdjdj"
SOLANA_ADDRESS = "DVaoLjuk8qsc3KbM84JoCHNSFLuVpwtLsD6ac6jWuzWx"

bot = telebot.TeleBot(BOT_TOKEN)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛒 Voir les services"))
menu.add(KeyboardButton("💬 Contacter le support"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bienvenue ! Choisis une option :", reply_markup=menu)

@bot.message_handler(func=lambda m: "services" in m.text.lower())
def services(message):
    txt = (
        "<b>📦 Services disponibles :</b>

"
        "🔹 Spam sur lien : 25€ / 1k
"
        "🔹 Technique Pristelle : 50€ (3 SIM remboursables)
"
        "🔹 Logs : Facebook, Amazon, Netflix, Mobiax → 10€ par log

"
        f"💰 Paiement Solana : <code>{SOLANA_ADDRESS}</code>
"
        f"📩 Contact : @{SUPPORT_USERNAME}"
    )
    bot.send_message(message.chat.id, txt, parse_mode="HTML")

@bot.message_handler(func=lambda m: "support" in m.text.lower())
def support(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Contacter le support", url=f"https://t.me/{SUPPORT_USERNAME}"))
    bot.send_message(message.chat.id, "Besoin d'aide ? Clique ci-dessous :", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Commande inconnue. Utilise le menu.", reply_markup=menu)

bot.infinity_polling()
