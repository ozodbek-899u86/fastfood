from aiogram import types

from loader import dp

WORDS = ['ahmoq', 'jinni', 'tentak']
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    for word in WORDS:
        if word in message.text.lower():
            await message.answer("So'kish mumkin emas!")

# @dp.message_handler(commands='id', commands_prefix='/')
# async def id()