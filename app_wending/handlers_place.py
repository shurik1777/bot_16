from aiogram import F, Router
from aiogram.types import CallbackQuery
import app_wending.keyboards as kb

router_four = Router()


@router_four.callback_query(F.data == 'restaurant')
async def place_restaurant(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Банкетный зал', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'unique')
async def place_unique(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Уникальное локация', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'garden')
async def place_garden(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Вечеринка в саду', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'modern')
async def place_modern(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Современная свадьба', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'classic')
async def place_classic(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Классическая свадьба', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'travel')
async def place_travel(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Свадьба в стиле путешествия', reply_markup=kb.next_back_style)


@router_four.callback_query(F.data == 'colors')
async def place_fason(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите цветовую палитру', reply_markup=kb.colors)


@router_four.callback_query(F.data == 'style')
async def season_summer(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Решили в другом стиле?', reply_markup=kb.style)
