from aiogram import F, Router
from aiogram.types import CallbackQuery
import app_wending.keyboards as kb

router_five = Router()


@router_five.callback_query(F.data == 'trapezoidal')
async def colors_trapezoidal(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Трапециевидный силуэт', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'naiad')
async def colors_naiad(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Русалка', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'sheath')
async def colors_sheath(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Футляр', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'ball_gown')
async def colors_ball_gown(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Бальное платье', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'overalls')
async def colors_overalls(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Комбинезон', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'retro')
async def colors_retro(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Ретро', reply_markup=kb.next_back_fashion)


@router_five.callback_query(F.data == 'fashion')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор фасона платьев', reply_markup=kb.fashion)


@router_five.callback_query(F.data == 'costume')
async def next_costume(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите костюм жениха', reply_markup=kb.costume)
