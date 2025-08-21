import os
from dotenv import load_dotenv

import telebot

from telebot import types

# Загрузка переменных окружения из файла .env

load_dotenv()

# Получение токена Telegram-бота из переменных окружения

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Создание экземпляра бота

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start

@bot.message_handler(commands=['start'])

def start(message):

    # Создание встроенной клавиатуры

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('Связаться с админом', url='https://t.me/milwgiv'))

    markup.add(types.InlineKeyboardButton('Другие марафоны Way Giver', url='https://t.me/addlist/qLaq0UdnBh80NDky'))

    # Отправка приветственного сообщения с клавиатурой

    bot.reply_to(

        message,

        f"Поздравляю, {message.from_user.first_name}!\n Вы попали на марафон по английскому от way giver! 🎯\n\n"

        "Бот Way Giver поможет проанализировать Ваш уровень и составит план обучения для тебя. "

        "Я надеюсь, что марафон поможет именно тебе, но не забывай, что многое зависит от твоего желания и упорства!\n\n"

        "Чтобы начать обучение отправьте команду /level \n\n"

        "Не забудьте, что у Вас подписка за звёзды обновляется каждый месяц",

        reply_markup=markup

    )

# Обработчики команд /level, /strong, /weak (аналогично, создают клавиатуры со ссылками и отправляют сообщения)

# ...

# Обработчик команды /task (запрашивает у пользователя результаты тестов)

@bot.message_handler(commands=['task'])

def start(message):

    bot.reply_to(

        message,

        f"{message.from_user.first_name}, отправьте результаты ваших тестов одной строчкой "

        "в таком порядке:\n\n A1, разговор, чтение (Первый тест, второй тест, третий)\n\n"

        "Всё написано через запятую с пробелом. Уровень владения языком написан с заглавной буквы, "

        "а сильные и слабые стороны - с маленькой."

    )

# Обработчик команды /manual

@bot.message_handler(commands=['manual'])

def start(message):

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('Получить материал для обучение', url='https://t.me/+cb8Jz1KpO0dhNWFi'))

    bot.reply_to(

        message,

        f"{message.from_user.first_name}, Вы узнали свой уровень знаний с помощью бота Way Giver!\n"

        "Для того чтобы найти подходящий материал сверьте выше отправленный уровень и название поста в канале\n\n"

        "Не забудьте, что Ваша подписка (на канал с материалом) за звёзды и обновляется каждый месяц",

        reply_markup=markup

    )

# Список доступных уровней и навыков

levels = ["А1", "А2", "В1", "В2", "С1", "С2"]

skills = ["чтение", "разговор", "грамматика"]

skills_numbers = {

    "чтение": "1",

    "разговор": "2",

    "грамматика": "3"

}

# Обработчик текстовых сообщений (анализ уровня и навыков)

@bot.message_handler(func=lambda message: not message.text.startswith('/'))

def handle_message(message):

    text = message.text.lower().strip()

    parts = [x.strip() for x in text.split(",")]

    if len(parts) >= 2:

        user_level = parts[0].upper()

        input_skills = parts[1:]

        if user_level not in levels:

            bot.reply_to(message, "Неверный уровень. Выберите один из: А1, А2, В1, В2, С1, С2")

            return

        for sk in input_skills:

            if sk not in skills:

                bot.reply_to(message, f"Навык '{sk}' неизвестен. Доступны: чтение, разговор, грамматика")

                return

        missing_skills = [sk for sk in skills if sk not in input_skills]

        full_skills = input_skills + missing_skills

        numbers = [skills_numbers[sk] for sk in full_skills]

        code = f"{user_level}-{'-'.join(numbers)}"

        bot.reply_to(message,

                     f"Ваш уровень: {code}\n"

                     "Вы узнали свой уровень знаний с помощью бота Way Giver!\n\n"

                     "Чтобы получить инструкцию по применению этого уровня отправьте /manual"

                     )

    else:

        bot.reply_to(message,

                     "Отправьте сообщение в формате:\n"

                     "А1(русская заглавная буква), чтение, грамматика (слова через запятую с пробелом и с маленькой буквы)"

                     )

# Обработчик фото (отправляет сообщение, что бот не умеет распознавать фото)

@bot.message_handler(content_types=['photo'])

def get_photo(message):

    bot.reply_to(message, 'Бот Way Giver English на данный момент не умеет распознавать фото')

# Запуск бота

bot.polling(none_stop=True)

