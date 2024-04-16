from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Старт квиза', callback_data='quiz'),
     InlineKeyboardButton(text='Результат', callback_data='result')],
    [InlineKeyboardButton(text='О боте', callback_data='about_b'),
     InlineKeyboardButton(text='О нас', callback_data='about')],
])


#################### КВеСТ #########################

seazons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💐         Весна         💐', callback_data='spring'),
     InlineKeyboardButton(text='💐         Лето          💐', callback_data='summer')],
    [InlineKeyboardButton(text='💐         Осень         💐', callback_data='autumn'),
     InlineKeyboardButton(text='💐         Зима          💐', callback_data='winter')],
])

next_back_seazon = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='seazons'),
     InlineKeyboardButton(text='Далее', callback_data='quantity')]])



# async def inline_about():
#     keyboard = InlineKeyboardBuilder()
#     keyboard.add(InlineKeyboardButton(text='Назад', callback_data='Назад'))
#     return keyboard.as_markup()


back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='Назад')]])
