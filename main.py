import os
import time
import telebot

# التوكن الخاص بك
BOT_TOKEN = "7999893111:AAGe_NUHgeelBTXK496jrHeug11vsiWQDKk"
bot = telebot.TeleBot(BOT_TOKEN)

# النص العلوي والسفلي حسب ما زودتني
TEXT_TOP = """قم بترجمة النص للعربي بما يلائم فيديو شورت مدته (    ) ثانية و حافظ على تدفق النص بسلاسة،قم باستبدال اسماء الاشخاص ان وجدت
ب(الرجل،المرأة،الفتاة،الطفل،الشاب......) و
هكذا،ساستخدم هذا النص لتوليد صوت بالذكاء
الاصطناعي لذلك اضف علامات الترقيم كالتعجب و
الفواصل و النقاط الشارحة و لا تضف اي نقطة الا في
النهاية النص:"""

TEXT_BOTTOM = """اريد ان يحتوي ردك على النص فقط بدون اي اضافة او تعليق او عبارات خدمة مثل ساقوم بما تريد او حاضر او ساترجم النص كما طلبت، اريد النص فقط."""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    reply = f"{TEXT_TOP}\n\n{user_text}\n\n{TEXT_BOTTOM}"
    bot.send_message(message.chat.id, reply)
    print("✅ تم تنفيذ المهمة. سيتم إيقاف البوت الآن.")
    time.sleep(1)
    os._exit(0)

print("🚀 البوت يعمل الآن وينتظر الرسائل...")
bot.polling()
