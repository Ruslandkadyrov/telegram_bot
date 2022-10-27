from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

def get_start_ikb()-> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=
        [
            [
                InlineKeyboardButton(text='Азаров', callback_data='Азаров'),
                InlineKeyboardButton(text='Баринов', callback_data='Баринов'),
                InlineKeyboardButton(text='Валиев', callback_data='Валиев'),
                InlineKeyboardButton(text='Валитов', callback_data='Валитов')
            ],
            [
                InlineKeyboardButton(text='Гайдуков', callback_data='Гайдуков'),
                InlineKeyboardButton(text='Глазунов', callback_data='Глазунов'),
                InlineKeyboardButton(text='Гребенников', callback_data='Гребенников'),
                InlineKeyboardButton(text='Губайдуллин', callback_data='Губайдуллин')
            ],
            [
                InlineKeyboardButton(text='Девятов', callback_data='Девятов'),
                InlineKeyboardButton(text='Зайдуллин', callback_data='Зайдуллин'),
                InlineKeyboardButton(text='Исаев', callback_data='Исаев'),
                InlineKeyboardButton(text='Кадыров', callback_data='Кадыров')
            ],
            [
                InlineKeyboardButton(text='Козлов', callback_data='Козлов'),
                InlineKeyboardButton(text='Коньков', callback_data='Коньков'),
                InlineKeyboardButton(text='Мурызин', callback_data='Мурызин'),
                InlineKeyboardButton(text='Мухаметов', callback_data='Мухаметов')
            ],
            [
                InlineKeyboardButton(text='Нечаев', callback_data='Нечаев'),
                InlineKeyboardButton(text='Плюснин', callback_data='Плюснин'),
                InlineKeyboardButton(text='Салихов', callback_data='Салихов'),
                InlineKeyboardButton(text='Тараканов', callback_data='Тараканов')
            ],
            [
                InlineKeyboardButton(text='Тепляков', callback_data='Тепляков')
            ],
            [
                InlineKeyboardButton(text='Истекает срок', callback_data='срок')
            ]

        ])
    return ikb



button_hi = KeyboardButton('Выбрать инженера')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_hi)
