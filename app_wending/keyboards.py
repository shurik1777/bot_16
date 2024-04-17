from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Старт квиза', callback_data='quiz'),
     InlineKeyboardButton(text='Результат', callback_data='result')],
    [InlineKeyboardButton(text='О боте', callback_data='about_b'),
     InlineKeyboardButton(text='О нас', callback_data='about')],
])

#################### Выбор сезона свадьбы #########################

seazons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💐         Весна         💐', callback_data='spring'),
     InlineKeyboardButton(text='💐         Лето          💐', callback_data='summer')],
    [InlineKeyboardButton(text='💐         Осень         💐', callback_data='autumn'),
     InlineKeyboardButton(text='💐         Зима          💐', callback_data='winter')],
    [InlineKeyboardButton(text='Назад', callback_data='Назад')],
])

next_back_seazon = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='seazons'),
     InlineKeyboardButton(text='Далее', callback_data='onward')]])

#################### Выбор количества участников свадьбы ##########
amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Только в двоем', callback_data='together'),
     InlineKeyboardButton(text='Только близкие', callback_data='folks')],
    [InlineKeyboardButton(text='До 100', callback_data='upto100'),
     InlineKeyboardButton(text='Более 100', callback_data='more100')],
    [InlineKeyboardButton(text='Назад', callback_data='seazons')],
])

next_back_amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='amount'),
     InlineKeyboardButton(text='Далее', callback_data='farther')]])
################### Клавиатура для возврата назад переиспользуется
back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='Назад')]])
