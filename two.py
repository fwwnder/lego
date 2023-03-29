import telegram
from three import menu, back

def first():
    buttons = [
        [telegram.KeyboardButton(menu[0])],
        [telegram.KeyboardButton(menu[1])],
        [telegram.KeyboardButton(menu[2])],
        [telegram.KeyboardButton(menu[3])],
    ]
    return telegram.ReplyKeyboardMarkup(
        buttons, resize_keyboard=True, one_time_keyboard=False
    )
def backing():
    reverse = ([
        [telegram.KeyboardButton(back[0])]
    ])
    return telegram.ReplyKeyboardMarkup(
        reverse, resize_keyboard=True, one_time_keyboard=False
    )


