from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import keyboards.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi, bro',
                         reply_markup= kb.settings)

@router.message(Command('get_info'))
async def cmd_start(message: Message):
    await message.answer(f'Hi, BRO! \nYour_ID: {message.from_user.id}\nYour_name: {message.from_user.first_name}',
                         reply_markup= await kb.user_list())

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Comand Help')

@router.message(F.text == 'Как дела?')
async def txt_how_are_you(message: Message):
    await message.answer('Ok')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID Photo:  {message.photo[-1].file_id }')

@router.message(Command('send_photo'))
async def send_message(message: Message):
    await message.answer_photo(photo= 'AgACAgIAAxkBAAMTZ4kkoQoRXmF7pOcB9UeGlNCrNiwAApjoMRs5-UlIytfWVd9JU_wBAAMCAAN5AAM2BA',
                               caption='Text_Photo')


"""Вызов новой ин. клавиатуры, answer"""
@router.callback_query(F.data == 'in_1')
async def in_1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('You press button 1', reply_markup= await kb.user_list())

"""Заменв ин. клавиатуры, edit_text"""
@router.callback_query(F.data == 'in_2')
async def in_2(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('You press button 2', reply_markup= await kb.user_list()) 

"""Сообщение поверх, 'You press button 3'"""
@router.callback_query(F.data == 'in_3')
async def in_3(callback: CallbackQuery):
    await callback.answer('You press button 3')
    await callback.message.answer('You press button 3',reply_markup= await kb.user_list())

"""Фиксированное сообщение поверх, 'You press button 3'"""
@router.callback_query(F.data == 'in_4')
async def in_4(callback: CallbackQuery):
    await callback.answer('You press button 4', show_alert=True)
    await callback.message.answer('You press button 4', reply_markup= await kb.user_list())