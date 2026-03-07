import telebot
from telebot import types

# التوكن تاعك
API_TOKEN = '8616115988:AAF5AJRRPDbcFdtpDrEeYw5heKdcHycFymM'
bot = telebot.TeleBot(API_TOKEN)

# --- 1. القائمة الرئيسية للخدمات ---
def services_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("فيسبوك 💙", callback_data="serv_fb"),
        types.InlineKeyboardButton("يوتيوب ❤️", callback_data="serv_yt"),
        types.InlineKeyboardButton("تيكتوك 🖤", callback_data="serv_tt"),
        types.InlineKeyboardButton("تيليجرام 🩵", callback_data="serv_tg"),
        types.InlineKeyboardButton("إنستغرام 📸", callback_data="serv_inst"),
        types.InlineKeyboardButton("تويتر (X) 🐦", callback_data="serv_tw"),
        types.InlineKeyboardButton("🔙 رجوع للقائمة", callback_data="main_menu")
    )
    return markup

# --- 2. قوائم الخدمات التفصيلية ---
def sub_services(platform):
    markup = types.InlineKeyboardMarkup(row_width=1)
    if platform == "fb":
        markup.add(
            types.InlineKeyboardButton("👥 متابعين حقيقية", callback_data="order_fake"),
            types.InlineKeyboardButton("👨‍👩‍👧‍👦 مشتركين مجموعة", callback_data="order_fake"),
            types.InlineKeyboardButton("👍 لايكات صفحة/بوست", callback_data="order_fake")
        )
    elif platform == "yt":
        markup.add(
            types.InlineKeyboardButton("🔥 مشتركين أرخص لدينا", callback_data="order_fake"),
            types.InlineKeyboardButton("👍 لايكات فيديو", callback_data="order_fake"),
            types.InlineKeyboardButton("👀 ساعات مشاهدة", callback_data="order_fake")
        )
    elif platform == "tt":
        markup.add(
            types.InlineKeyboardButton("👤 مشاهدات ملف شخصي", callback_data="order_fake"),
            types.InlineKeyboardButton("🎬 مشاهدات بوست", callback_data="order_fake"),
            types.InlineKeyboardButton("⚡ تكبيس لايف", callback_data="order_fake"),
            types.InlineKeyboardButton("💖 متابعين عرب", callback_data="order_fake")
        )
    elif platform == "tg":
        markup.add(
            types.InlineKeyboardButton("🔥 تفاعلات (Reactions)", callback_data="order_fake"),
            types.InlineKeyboardButton("📢 مشتركين قناة", callback_data="order_fake"),
            types.InlineKeyboardButton("👁️ مشاهدات آخر 10 منشورات", callback_data="order_fake")
        )
    elif platform == "inst":
        markup.add(
            types.InlineKeyboardButton("🌟 متابعين ضمان 30 يوم", callback_data="order_fake"),
            types.InlineKeyboardButton("❤️ لايكات سريعة", callback_data="order_fake"),
            types.InlineKeyboardButton("📱 مشاهدات ستوري/Reels", callback_data="order_fake")
        )
    
    markup.add(types.InlineKeyboardButton("🔙 رجوع للخدمات", callback_data="services"))
    return markup

# --- 3. معالجة الضغطات (Callback Query) ---
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # الدخول لقسم الخدمات
    if call.data == "services":
        bot.edit_message_text("📂 | اختر المنصة التي تريد تزويدها:", 
                              call.message.chat.id, call.message.message_id, reply_markup=services_markup())

    # الدخول للخدمات الفرعية
    elif call.data.startswith("serv_"):
        platform = call.data.split("_")[1]
        platforms_names = {"fb": "فيسبوك 💙", "yt": "يوتيوب ❤️", "tt": "تيكتوك 🖤", "tg": "تيليجرام 🩵", "inst": "إنستغرام 📸"}
        bot.edit_message_text(f"🛠️ | خدمات {platforms_names.get(platform, '')}\nاختر نوع الخدمة المطلوب:", 
                              call.message.chat.id, call.message.message_id, reply_markup=sub_services(platform))

    # خدعة الطلب (الخطأ الوهمي)
    elif call.data == "order_fake":
        bot.answer_callback_query(call.id, "⚠️ خطأ: رصيد النقاط غير كافٍ أو السيرفر مشغول حالياً.", show_alert=True)

    # الرجوع للقائمة الرئيسية
    elif call.data == "main_menu":
        bot.edit_message_text("🏠 القائمة الرئيسية لبوت طلباتي", call.message.chat.id, call.message.message_id)
        # هنا تقدر تعاود تبعت الـ start_markup

print("البوت الاحترافي مع جميع الأقسام شغال..")
bot.polling(none_stop=True)
