from settings import settings
import discord
from discord.ext import commands
import random
import asyncio


intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

def get_global_warming_quote():
    quotes = [
        "Измени мир, начиная с себя.",
        "Будь изменением, которое ты хочешь увидеть в мире.",
        "Каждый шаг к экологии — это шаг к будущему.",
        "Сохраняй природу, чтобы сохранить себя.",
        "Мы не наследовали землю у предков, мы одолжили ее у потомков.",
    ]
    return random.choice(quotes)



questions_answers = {
    "Какой газ способствует парниковому эффекту?": "углекислый газ",
    "Какие действия помогают снизить выбросы парниковых газов?": "переход на общественный транспорт, использование альтернативных источников энергии",
    "Что такое парниковый эффект?": "явление задержки тепла в атмосфере из-за увеличения уровня парниковых газов",
    "Какие последствия может иметь глобальное потепление для климата Земли?": "подъем уровня моря, изменения в экосистемах, экстремальные погодные условия",
    "Что такое парниковые газы и как они влияют на климат Земли?": "парниковые газы - это газы, которые задерживают тепло в атмосфере",
    "Какие регионы мира могут быть особенно уязвимы для последствий глобального потепления?": "арктические регионы, островные нации, пустыни и субтропические районы",
}


def send_memes():
    memes = ["image/2f8f9c2e82caec2f27060df8ac01751c.jpg", "image/6c97951fee074781bbd9427bc4293292.jpg", "image/Приколы-для-даунов-разное-5391910.jpeg", "image/смешные-демотиваторы-auto-26646.jpeg" , "image\scale_1200.jpg " , ]
    meme = random.choice(memes)
    return meme

@bot.command()
async def quiz(ctx):
    quiz_info = "Добро пожаловать в викторину по теме изменения климата! Ответьте на вопросы, чтобы узнать больше о важных аспектах изменения климата."
    await ctx.send(quiz_info)

    num_questions = 3  
    correct_answers = 0

    for _ in range(num_questions):
        question = random.choice(list(questions_answers.keys()))
        await ctx.send(question)

        def check(m):
            return m.author == ctx.author and m.content.lower() == questions_answers[question].lower()

        try:
            response = await bot.wait_for('message', timeout=30.0, check=check)
            await ctx.send('Правильный ответ!')
            correct_answers += 1
        except asyncio.TimeoutError:
            await ctx.send('Время вышло, правильный ответ: {}'.format(questions_answers[question]))

    await ctx.send(f'Викторина завершена! Вы ответили правильно на {correct_answers} из {num_questions} вопросов.')


@bot.command()
async def info (ctx):
    info_message = "Информация о борьбе с изменением климата: чтобы помочь бороться с изменением климата, вы можете: перейти на общественный транспорт и использовать альтернативные источники энергии."
    await ctx.send(info_message)


@bot.command()
async def helps(ctx):
    help_message = "Список доступных команд:\n"
    
    help_message += "$quiz - Начать викторину по теме изменения климата.\n"
    help_message += "$info - Получить информацию о борьбе с изменением климата.\n"
    help_message += "$send_meme - Отправить случайный мем.\n"
    help_message += "$quote - Отправит случайную цитату.\n"

    await ctx.send(help_message)


@bot.event
async def on_ready():
    print('Залогинен как {0.user}'.format(bot))

@bot.command()
async def send_meme(ctx):
    meme = send_memes()
    await ctx.send(file=discord.File(meme))

@bot.command()
async def quote(ctx):
    random_quote = get_global_warming_quote()
    await ctx.send(random_quote)





bot.run(settings["TOKEN"])





