from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandPrivacy, CommandSettings

from loader import dp

@dp.message_handler(CommandSettings())
async def bot_help(message: types.Message):
    text = ("/ro -- 5 daqiqaga read only qilish\n"
            "/ro 6 -- daqiqasini korsaaatib read only qilish\n"
            "/ro 9 text -- sababini korsatib read only qilish\n"
            "/ban - guruhdan haydash, qatib qoshiltirmaslik\n"
            "/unban - qora royxatdan chiqarish\n")
    await message.answer(text)

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))

