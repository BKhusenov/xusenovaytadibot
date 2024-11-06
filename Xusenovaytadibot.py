from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram bot tokeni va kanallaringiz ID'lari
TOKEN = "7558431780:AAGquk2sUn7Mnp7317-rpgj1wpPdiCilNSw"  # O'zingizning tokeningizni o'rnating
PUBLIC_CHANNEL_ID = "-1002097136466"       # Umumiy kanal ID'si
PRIVATE_CHANNEL_ID = "-1001588823732"      # Maxfiy kanal ID'si

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Salom! \n Siz anonim xabar yozishingiz mumkin. \n Xabaringiz Xusenovaytadi kanalda anonim tarzda chop etiladi.")

# Foydalanuvchidan kelgan xabarni qabul qilish uchun funksiya
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    text = update.message.text

    # 1. Xabarni umumiy kanalga anonim tarzda yuborish
    message_to_public = f"Sizga Anonim xabar:\n\n{text}"
    await context.bot.send_message(chat_id=PUBLIC_CHANNEL_ID, text=message_to_public)

    # 2. Xabarni foydalanuvchi ma'lumotlari bilan birgalikda maxfiy kanalga yuborish
    message_to_private = f"Xabar:\n\n{text}\n\n👤 Foydalanuvchi: @{username} (ID: {user_id})"
    await context.bot.send_message(chat_id=PRIVATE_CHANNEL_ID, text=message_to_private)

    # Foydalanuvchiga tasdiqlovchi xabar yuborish
    await update.message.reply_text("Xabaringiz anonim tarzda kanalda chop etildi!")

# Asosiy dastur
def main():
    # Bot dasturini ishga tushirish
    application = ApplicationBuilder().token(TOKEN).build()

    # Komandalar va xabarlar uchun handlerlarni qo'shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == "__main__":
    main()
