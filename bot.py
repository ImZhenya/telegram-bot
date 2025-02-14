import telebot
from datetime import datetime, timedelta

TOKEN = "7655082967:AAFRDZFdRs7yhDBTOZ5ovFjv-ea6Eo9IBFE"  

bot = telebot.TeleBot(TOKEN)
time_shift = 0  # Сдвиг времени (по умолчанию 0 часов)

@bot.message_handler(commands=['shift'])
def set_time_shift(message):
    global time_shift
    try:
        shift = int(message.text.split()[1])  # Получаем число после команды
        time_shift = shift
        bot.reply_to(message, f"Сдвиг времени установлен на {time_shift} часов.")
    except (IndexError, ValueError):
        bot.reply_to(message, "Ошибка! Введи команду в формате: /shift X, где X — число часов (например, `/shift -3`).")

@bot.message_handler(func=lambda message: True)
def modify_time(message):
    new_time = datetime.now() + timedelta(hours=time_shift)
    formatted_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
    bot.send_message(message.chat.id, f"({formatted_time}) {message.text}")

bot.polling()