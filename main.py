import os
import telebot
from flask import Flask, request

BOT_TOKEN = "7999893111:AAGe_NUHgeelBTXK496jrHeug11vsiWQDKk"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

TEXT_TOP = """قم بترجمة النص للعربي بما يلائم فيديو شورت مدته (    ) ثانية و حافظ على تدفق النص بسلاسة،قم باستبدال اسماء الاشخاص ان وجدت 
ب(الرجل،المرأة،الفتاة،الطفل،الشاب......) و 
هكذا،ساستخدم هذا النص لتوليد صوت بالذكاء 
الاصطناعي لذلك اضف علامات الترقيم بما تراه مناسبا و لا تضف اي نقطة الا في 
النهاية
النص:"""

TEXT_BOTTOM = """اريد ان يحتوي ردك على النص فقط بدون اي اضافة او تعليق او عبارات خدمة مثل ساقوم بما تريد او حاضر او ساترجم النص كما طلبت، اريد النص فقط."""

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    reply = f"{TEXT_TOP}\n\n{user_text}\n\n{TEXT_BOTTOM}"
    bot.send_message(message.chat.id, reply)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
