import sql_for_bot
import logging
from aiogram import Bot, Dispatcher, types, executor
from keyboards import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token="")
dp = Dispatcher(bot)

async def on_startup(_):
    await sql_for_bot.db_connect()
    print('Подключение к БД выполнено успешно')

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer('Выберите инженера', reply_markup=get_start_ikb())

@dp.callback_query_handler(text='срок')
async def cb_get_term(callback: types.CallbackQuery):
    term = await sql_for_bot.term_of_the_certificate()
    await callback.message.answer(term, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Азаров')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Азаров Евгений Федорович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Баринов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Баринов Сергей Борисович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Валиев')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Валиев Фларит Фаритович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Валитов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Валитов Марат Ревинерович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Гайдуков')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Гайдуков Андрей Иванович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Глазунов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Глазунов Юрий Николаевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Гребенников')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Гребенников Александр Александрович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Губайдуллин')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Губайдуллин Артур Радикович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Губайдуллин')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Губайдуллин Артур Радикович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Девятов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Девятов Шамиль Раилевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Зайдуллин')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Зайдуллин Рустам Шамилевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Исаев')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Исаев Алексей Владимирович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Кадыров')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Кадыров Руслан Ринатович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Козлов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Козлов Денис Васильевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Коньков')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Коньков Владимир Владимирович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Мурызин')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Мурызин Алексей Юрьевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Мухаметов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Мухаметов Тимур Мунирович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Нечаев')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Нечаев Максим Николаевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Плюснин')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Плюснин Максим Евгеньевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Салихов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Салихов Газимагомед Магомедович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Тараканов')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Тараканов Валерий Владимирович')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.callback_query_handler(text='Тепляков')
async def cb_get_all_ingeners(callback: types.CallbackQuery):
    ingerers = await sql_for_bot.get_all_ingeners('Тепляков Алексей Николаевич')
    await callback.message.answer(ingerers, reply_markup=greet_kb)
    await callback.answer()

@dp.message_handler()
async def cmd_choose(message: types.Message):
    await message.answer('Выберите инженера', reply_markup=get_start_ikb())


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)

