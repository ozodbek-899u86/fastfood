from aiogram.types import Message
from loader import dp
from keyboards.default.catigorie import *
@dp.message_handler(text='🥤suvlar')
async def drinkcatagory(message: Message):
    await message.answer('katigoryani tanlang', reply_markup=drinkcatagory)
