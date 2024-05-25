from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пригласить друга"),
            KeyboardButton(text="Мои рефералы")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить гео", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True),
            KeyboardButton(text="Создать викторину",
                           request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="НАЗАД")
        ]
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="PREMIUM GIRLS"),
            KeyboardButton(text="RECOMMEND GIRLS"),
        ],
        [
            KeyboardButton(text="SHOW GIRLS"),
        ],
        [
            KeyboardButton(text="Premium Code"),
            KeyboardButton(text="Change Country")
        ],
        [
            KeyboardButton(text="Contact Us"),
        ]
    ],
    resize_keyboard=True
)


rmk = ReplyKeyboardRemove()

