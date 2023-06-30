from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


FORBIDDEN_PHRASE = [
    'ahmoq',
    'telba',
]
import asyncio
from contextlib import suppress
from filters import IsGroup, AdminFilter

from aiogram import types
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound)

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()
@dp.message_handler(filters.Text(contains='https:/', ignore_case=True))
async def text(msg: types.Message):
    await msg.delete()
@dp.message_handler(text_contains='@')
async def text_example(msg: types.Message):
    await msg.delete()

# @dp.message_handler()
# async def text_example(msg: types.Message):
#     await msg.reply("So'kish mumkin emas!")

@dp.message_handler(filters.Text(equals='assalom alaykum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')

@dp.message_handler(filters.Text(contains='assalom', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Waalaykum assalom')

# boshqa parametrlar
# startswith
# endswith