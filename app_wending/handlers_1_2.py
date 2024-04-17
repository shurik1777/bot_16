from aiogram import F, Router
from aiogram.types import CallbackQuery
import app_wending.keyboards as kb

router_one = Router()

""" Первый под уровень квиза - блок сезонов """


@router_one.callback_query(F.data == 'spring')
async def season_spring(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Весна', reply_markup=kb.next_back_seazon)


@router_one.callback_query(F.data == 'summer')
async def season_summer(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Лето', reply_markup=kb.next_back_seazon)


@router_one.callback_query(F.data == 'autumn')
async def season_autumn(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Осень', reply_markup=kb.next_back_seazon)


@router_one.callback_query(F.data == 'winter')
async def season_winter(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text('Зима', reply_markup=kb.next_back_seazon)


@router_one.callback_query(F.data.startswith('seazons'))
async def back_season(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вернулись на выбор сезона', reply_markup=kb.seazons)


@router_one.callback_query(F.data.startswith('onward'))
async def season_spring(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы попали в Выбор кол-во гостей', reply_markup=kb.amount)


""" Второй уровень квиза - Количество гостей """


@router_one.callback_query(F.data == 'together')
async def amount_together(callback: CallbackQuery):
    await callback.answer('Только в двоем')
    await callback.message.edit_text('Только в двоем', reply_markup=kb.next_back_amount)


@router_one.callback_query(F.data == 'folks')
async def amount_folks(callback: CallbackQuery):
    await callback.answer('Только близкие')
    await callback.message.edit_text('Только близкие', reply_markup=kb.next_back_amount)


@router_one.callback_query(F.data == 'upto100')
async def amount_upto100(callback: CallbackQuery):
    await callback.answer('До 100')
    await callback.message.edit_text('До 100', reply_markup=kb.next_back_amount)


@router_one.callback_query(F.data == 'more100')
async def amount_more100(callback: CallbackQuery):
    await callback.answer('Более 100')
    await callback.message.edit_text('Более 100', reply_markup=kb.next_back_amount)


@router_one.callback_query(F.data.startswith('farther'))
async def amount_farther(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выбор стиля свадьбы', reply_markup=kb.style)


@router_one.callback_query(F.data.startswith('amount'))
async def back_about_b(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Вы передумали?', reply_markup=kb.amount)
