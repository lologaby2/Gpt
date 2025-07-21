import os
import time
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")  # نحصل على التوكن من متغير البيئة
bot = telebot.TeleBot(BOT_TOKEN)

TEXT_TOP = "🔼 هذا هو النص الذي فوق"
TEXT_BOTTOM = "🔽 هذا هو النص الذي تحت"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    reply = f"{TEXT_TOP}\n{user_text}\n{TEXT_BOTTOM}"
    bot.send_message(message.chat.id, reply)
    print("✅ تم تنفيذ المهمة. سيتم إيقاف البوت الآن.")
    time.sleep(1)
    os._exit(0)

print("🚀 البوت يعمل الآن...")
bot.polling()
