from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def drinkscategorybutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='🥤 Coca cola'),
        KeyboardButton(text='🥤 Pepsi'),

    )
    markup.add(
        KeyboardButton(text='🥤 Fanta'),

    )
    markup.add(
        KeyboardButton(text='🥤 Dinay'),
        KeyboardButton(text='🥤 Dena')
    )
    return markup