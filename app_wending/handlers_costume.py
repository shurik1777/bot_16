from aiogram import F, Router
from aiogram.types import CallbackQuery
import app_wending.keyboards as kb

router_seven = Router()


@router_seven.callback_query(F.data == 'classic')
async def costume_classic(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Классика', reply_markup=kb.next_back_costume)


@router_seven.callback_query(F.data == 'tuxedo')
async def costume_tuxedo(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Смокинг', reply_markup=kb.next_back_costume)


@router_seven.callback_query(F.data == 'casual')
async def costume_casual(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Кэжуал', reply_markup=kb.next_back_costume)


@router_seven.callback_query(F.data == 'something')
async def costume_something(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Современный костюм', reply_markup=kb.next_back_costume)


@router_seven.callback_query(F.data == 'costume')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор фасона платьев', reply_markup=kb.costume)


# @router_seven.callback_query(F.data == 'fashion')
# async def next_fashion(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text(
#         'Выберите костюм жениха', reply_markup=kb.fashion)
