# from aiogram import types
#
# from loader import dp
# from filters import IsPrivate,AdminFilter
# from aiogram.dispatcher.filters import Command
# from handlers.groups.sql import db
#
# # # IsReplyFilter
# # @dp.message_handler(commands='user_id')
# # async def reply_filter_example(msg: types.Message):
# #     await msg.answer(msg.from_user.id)
# #
#
# # IsSenderContact
# @dp.message_handler(content_types='contact', is_sender_contact=True)
# # @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
# async def sender_contact_example(msg: types.Message):
#     await msg.answer('Rahmat, kontaktingiz qabul qilindi!')

#
# # ForwardedMessageFilter
# @dp.message_handler(is_forwarded=True)
# async def forwarded_example(msg: types.Message):
#     # await msg.answer('Birovning xabarini menga yuborayapsizmi?')
#     await msg.delete()
#
# @dp.message_handler(IsPrivate(), Command('statis', prefixes='!/'), AdminFilter())
# async def statis(message: types.Message):
#     cursor = db.cursor()
#     try:
#         if len(message.text) == 2:
#             _, user_id = message.text.split()
#             cursor.execute("""SELECT * FROM users WHERE user_id = ?""", (user_id, ))
#             users = cursor.fetchall()
#             await message.answer(f"Taklif qilgan foydalauvchi soni: {len(users)}")
#     except:
#         await message.answer('ERROR')
