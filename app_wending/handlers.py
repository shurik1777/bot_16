from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app_wending.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! {message.from_user.username}',
                         reply_markup=kb.main)


#################### Первый уровень квиза - выбор сезона #########################
@router.callback_query(F.data == 'quiz')
async def seazons_spring(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Выбор сезона', reply_markup=kb.seazons)


#################### Первый под уровень квиза - блок сезонов #########################
@router.callback_query(F.data == 'spring')
async def seazons_spring(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Весна', reply_markup=kb.next_back_seazon)


@router.callback_query(F.data == 'summer')
async def seazons_summer(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Лето', reply_markup=kb.next_back_seazon)


@router.callback_query(F.data == 'autumn')
async def seazons_autumn(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Осень', reply_markup=kb.next_back_seazon)


@router.callback_query(F.data == 'winter')
async def seazons_winter(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Зима', reply_markup=kb.next_back_seazon)


@router.callback_query(F.data.startswith('seazons'))
async def back_seazons(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вернулись на выбор сезона', reply_markup=kb.seazons)


#################### Второй уровень квиза - Количество гостей #########################


@router.callback_query(F.data == 'about')
async def main_about(callback: CallbackQuery):
    await callback.answer('Вы выбрали "О нас"')
    await callback.message.edit_text('Супер команда специалистов из ГБ', reply_markup=kb.back)


@router.callback_query(F.data == 'about_b')
async def main_about_b(callback: CallbackQuery):
    await callback.answer()
    # await callback.message.edit_text('Бод помогает устроить вашу свадьбу', reply_markup=await kb.inline_about())
    await callback.message.edit_text('Бод помогает устроить вашу свадьбу', reply_markup=kb.back)


@router.callback_query(F.data.startswith('Назад'))
async def back_about_b(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('И снова привет', reply_markup=kb.main)
