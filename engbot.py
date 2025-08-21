import os

from dotenv import load_dotenv

import telebot

from telebot import types


load_dotenv()


TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])

def start(message):



    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('Связаться с админом', url='https://t.me/milwgiv'))

    markup.add(types.InlineKeyboardButton('Другие марафоны Way Giver', url='https://t.me/addlist/qLaq0UdnBh80NDky'))



    bot.reply_to(

        message,

        f"Поздравляю, {message.from_user.first_name}!\n Вы попали на марафон по английскому от way giver! 🎯\n\n"+

        "Бот Way Giver поможет проанализировать Ваш уровень и составит план обучения для тебя. "+

        "Я надеюсь, что марафон поможет именно тебе, но не забывай, что многое зависит от твоего желания и упорства!\n\n"+

        "Чтобы начать обучение отправьте команду /level \n\n"+

        "Не забудьте, что у Вас подписка за звёзды обновляется каждый месяц",

        reply_markup=markup

    )



@bot.message_handler(commands=['level'])

def level(message):

    markup = types.InlineKeyboardMarkup()

    bt1 = types.InlineKeyboardButton('Test Your English (British Council)', url='https://learnenglish.britishcouncil.org/english-levels/online-english-level-test')

    bt2 = types.InlineKeyboardButton('English Level Test (Cambridge)', url='https://www.cambridgeenglish.org/test-your-english/')

    markup.add(bt1, bt2)

    bt3 = types.InlineKeyboardButton('EF SET', url='https://www.efset.org/')

    bt4 = types.InlineKeyboardButton('LanguageLevel', url='https://www.languagelevel.com/english/')

    markup.add(bt3, bt4)

    text = ("Знание иностранного языка часто определяют от уровня A1 до близкого к уровню носителей языка C2.\n"+

            "Каждой ступени соответствует набор навыков в чтении, восприятии на слух, устной и письменной речи.\n"+

            "Для дальнейшей работы нам надо определиться с вашим уровнем знаний.\n"+

            "Для того, чтобы приступить к следующему анализу отправьте команду /strong \n"+

            "Если вы уже знаете свой уровень — отлично, если нет — рекомендуем пройти тесты.\n\n"+

            "✔️ Проверенные сайты для проверки уровня:")

    bot.send_message(message.chat.id, text, reply_markup=markup, disable_web_page_preview=True)

@bot.message_handler(commands=['strong'])

def level(message):

    markup = types.InlineKeyboardMarkup()

    bt1 = types.InlineKeyboardButton('Flo-Joe', url='https://www.flo-joe.co.uk/')

    bt2 = types.InlineKeyboardButton('BBC Learning English', url='https://www.bbc.co.uk/learningenglish')

    markup.add(bt1, bt2)

    bt3 = types.InlineKeyboardButton('EnglishGrammar.org', url='https://www.englishgrammar.org/quizzes/')

    bt4 = types.InlineKeyboardButton('Speechling  ', url='https://speechling.com/ru/')

    markup.add(bt3, bt4)

    text = ("Знание своих сильных сторон в английском (чтение, разговор, грамматика) помогает эффективно планировать обучение и сосредоточиться на развитии слабых навыков. Это повышает мотивацию, так как видно прогресс и области, где уже есть успехи. Кроме того, понимание сильных сторон позволяет использовать их в реальных ситуациях для более уверенного общения и понимания языка.\n"+

            "Для того, чтобы приступить к следующему анализу отправьте команду /weak \n"+

            "Если вы уже знаете свои сильные стороны — отлично, если нет — рекомендуем пройти тесты.\n\n"+

            "✔️ Проверенные сайты для анализа сильных сторон:")

    bot.send_message(message.chat.id, text, reply_markup=markup, disable_web_page_preview=True)

@bot.message_handler(commands=['weak'])

def level(message):

    markup = types.InlineKeyboardMarkup()

    bt1 = types.InlineKeyboardButton('Grammarly', url='https://app.grammarly.com/')

    bt2 = types.InlineKeyboardButton('Lingua.com', url='https://lingua.com/english/')

    markup.add(bt1, bt2)

    bt3 = types.InlineKeyboardButton('English-Test.net', url='https://www.english-test.net/')

    bt4 = types.InlineKeyboardButton('Dictation.io', url='https://dictation.io/speech')

    markup.add(bt3, bt4)

    text = ("Знание своих слабых сторон в английском (чтение, разговор, грамматика) помогает определить, на что нужно обратить больше внимания при изучении. Это позволяет строить более эффективный план обучения и избегать повторения ошибок. Осознание слабых мест стимулирует постоянное развитие и улучшение навыков, что ведёт к уверенности в языке и более быстрому прогрессу.\n"+

            "Для того, чтобы приступить к следующему анализу отправьте команду /task \n"+

            "Если вы уже знаете свои сильные стороны — отлично, если нет — рекомендуем пройти тесты.\n\n"+

            "✔️ Проверенные сайты для анализа сильных сторон:")

    bot.send_message(message.chat.id, text, reply_markup=markup, disable_web_page_preview=True)



@bot.message_handler(commands=['task'])

def start(message):

    bot.reply_to(

        message,

        f"{message.from_user.first_name}, отправьте результаты ваших тестов одной строчкой "+

        "в таком порядке:\n\n A1, разговор, чтение (Первый тест, второй тест, третий)\n\n"+

        "Всё написано через запятую с пробелом. Уровень владения языком написан с заглавной буквы, "+

        "а сильные и слабые стороны - с маленькой."

    )



@bot.message_handler(commands=['manual'])

def start(message):

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('Получить материал для обучение', url='https://t.me/+cb8Jz1KpO0dhNWFi'))

    bot.reply_to(

        message,

        f"{message.from_user.first_name}, Вы узнали свой уровень знаний с помощью бота Way Giver!\n"+

        "Для того чтобы найти подходящий материал сверьте выше отправленный уровень и название поста в канале\n\n"+

        "Не забудьте, что Ваша подписка (на канал с материалом) за звёзды и обновляется каждый месяц",

        reply_markup=markup

    )



levels = ["А1", "А2", "В1", "В2", "С1", "С2"]

skills = ["чтение", "разговор", "грамматика"]

skills_numbers = {

    "чтение": "1",

    "разговор": "2",

    "грамматика": "3"

}



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

                     f"Ваш уровень: {code}\n"+

                     "Вы узнали свой уровень знаний с помощью бота Way Giver!\n\n"+

                     "Чтобы получить инструкцию по применению этого уровня отправьте /manual"

                     )

    else:

        bot.reply_to(message,

                     "Отправьте сообщение в формате:\n"+

                     "А1(русская заглавная буква), чтение, грамматика (слова через запятую с пробелом и с маленькой буквы)"

                     )


@bot.message_handler(content_types=['photo'])

def get_photo(message):

    bot.reply_to(message, 'Бот Way Giver English на данный момент не умеет распознавать фото')


bot.polling(none_stop=True)

