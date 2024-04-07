import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

questions_answers = {
    "Какой газ способствует парниковому эффекту?": "углекислый газ",
    "Какие действия помогают снизить выбросы парниковых газов?": "переход на общественный транспорт, использование альтернативных источников энергии",
    "Что такое парниковый эффект?": "явление задержки тепла в атмосфере из-за увеличения уровня парниковых газов",
    "Какие последствия может иметь глобальное потепление для климата Земли?": "подъем уровня моря, изменения в экосистемах, экстремальные погодные условия",
    "Что такое парниковые газы и как они влияют на климат Земли?": "парниковые газы - это газы, которые задерживают тепло в атмосфере",
    "Какие регионы мира могут быть особенно уязвимы для последствий глобального потепления?": "арктические регионы, островные нации, пустыни и субтропические районы",
}

def send_memes():
    memes = ["image/2f8f9c2e82caec2f27060df8ac01751c.jpg", "image/6c97951fee074781bbd9427bc4293292.jpg", "image/Приколы-для-даунов-разное-5391910.jpeg", "image/смешные-демотиваторы-auto-26646.jpeg"]
    meme = random.choice(memes)
    return meme

@bot.command()
async def quiz(ctx):
    question = random.choice(list(questions_answers.keys()))
    await ctx.send(question)

    def check(m):
        return m.author == ctx.author and m.content.lower() == questions_answers[question].lower()

    try:
        response = await bot.wait_for('message', timeout=30.0, check=check)
        await ctx.send('Правильный ответ!')
    except asyncio.TimeoutError:
        await ctx.send('Время вышло, правильный ответ: {}'.format(questions_answers[question]))

@bot.command()
async def info(ctx):
    info_message = "Информация о борьбе с изменением климата: чтобы помочь бороться с изменением климата, вы можете: перейти на общественный транспорт и использовать альтернативные источники энергии."
    await ctx.send(info_message)

@bot.event
async def on_ready():
    print('Залогинен как {0.user}'.format(bot))

@bot.command()
async def send_meme(ctx):
    meme = send_memes()
    await ctx.send(file=discord.File(meme))






bot.run('MTIyNjQ2MzEyNjc1MzY0NDY0NQ.GyowA7.dL4gLcSYNKT2Qcx0Dy0kPZtQSpIH2VurJuQAx8')






