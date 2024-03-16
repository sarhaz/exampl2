import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from main import Database
from default_keyboard import menu_keyboard, inside_ce, inside_gd, inside_prg, inside_l, inside_tr, computer_engineering, graphic_design, programming, trading, logistics
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = int(message.chat.id)
    check_query = f"""SELECT * FROM users WHERE chat_id = {chat_id}"""
    if len(Database.connect(check_query, "select")) >= 1:
        await message.answer_sticker("CAACAgIAAxkBAAIBAmX1ztnrEDndIeCFINOgK3rbKAeLAAI4CwACTuSZSzKxR9LZT4zQNAQ")
        await message.answer(f"""Hello @{username} Welcome to the new format platform! Organized and new lessons are waiting for you. Choose one of the sections below""", reply_markup=menu_keyboard)

    else:
        print(f"username: {username}")
        query = f"""INSERT INTO users (username, first_name, last_name,chat_id) VALUES ('{username}', '{first_name}', '{last_name}', {chat_id})"""
        Database.connect(query, "insert")
        print(f"information about {username} is inserted")
        await message.answer_sticker("CAACAgIAAxkBAAIBAmX1ztnrEDndIeCFINOgK3rbKAeLAAI4CwACTuSZSzKxR9LZT4zQNAQ")
        await message.answer(f"Hello @{username}", reply_markup=menu_keyboard)


@dp.message_handler(commands=['data'])
async def data(message: types.Message):
    chat_id = message.chat.id
    query_users = f"""SELECT * FROM users WHERE chat_id = {chat_id}"""
    data1 = Database.connect(query_users, "select")
    print(data1)
    await message.answer(f"""
    Hello {data1[0][1]}
    Your Username {data1[0][2]}""")


@dp.message_handler(lambda message: message.text == "Computer Engineering")
async def computer_engineering1(message: types.Message):
    await message.answer("Choose one of these options", reply_markup=computer_engineering)


@dp.message_handler(lambda message: message.text == "Graphic design")
async def graphic_design1(message: types.Message):
    await message.answer("Choose one of these options", reply_markup=graphic_design)


@dp.message_handler(lambda message: message.text == "Programming")
async def programming1(message: types.Message):
    await message.answer("Choose one of these options", reply_markup=programming)


@dp.message_handler(lambda message: message.text == "Trading")
async def trading1(message: types.Message):
    await message.answer("Choose one of these options", reply_markup=trading)


@dp.message_handler(lambda message: message.text == "Logistics")
async def logistics1(message: types.Message):
    await message.answer("Choose one of the courses", reply_markup=logistics)


@dp.message_handler(lambda message: message.text == "Back")
async def back(message: types.Message):
    await message.answer("Choose one of the courses", reply_markup=menu_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
