from libary import *

main_kb = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text='/selectSong'),
            KeyboardButton(text='/findSong'),
        ],
        [
            KeyboardButton(text='/help'),
            KeyboardButton(text='/creaters'),

        ],
        [
            KeyboardButton(text='/aboutBot')
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)