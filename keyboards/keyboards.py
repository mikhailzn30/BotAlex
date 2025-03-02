from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')], 
    [KeyboardButton(text='Info'), KeyboardButton(text='Контакты')]
],
                    resize_keyboard=True,
                    input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='in_1'), InlineKeyboardButton(text='2', callback_data='in_2')],
    [InlineKeyboardButton(text='3', callback_data='in_3'), InlineKeyboardButton(text='4', callback_data='in_4')]
])


users = ['Alex', 'Miha', 'Miri', 'vlad', 'Kirill', 'Fred', 'Roman']
async def user_list():
    keyboard= InlineKeyboardBuilder()
    for user in users:
        keyboard.add(InlineKeyboardButton(text=user, url='https://steamuserimages-a.akamaihd.net/ugc/1691648011766066213/E0113D90A80E9C31A0C8A166D50B3D84DD5A3389/?imw=512&imh=341&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true'))
    return keyboard.adjust(1).as_markup()