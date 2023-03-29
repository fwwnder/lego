from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import(
    CallbackContext,
    Updater,
    PicklePersistence,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    CommandHandler
)
from four import token
from two import first, backing
from three import menu, back

def start(update: Update, context = CallbackContext):
    update.message.reply_text(
        f'Здравствуйте, {update.effective_user.username}',
        reply_markup=first()
    )

def backo(update: Update, context: CallbackContext):
     update.message.reply_text(
          text='назад'
     )
     reply_markup = backing()

def location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Где мы находимся'
    )
    update.message.reply_location(
        longitude=42.8528079052402,
        latitude=74.60782708444705,
        reply_to_message_id=msg.message_id
    )

def menus(update: Update, context = CallbackContext):
        update.message.reply_text(
             text = 'наше меню'
        )
        context.bot.send_photo(
            update.effective_chat.id,
            photo=open('images.jpg', 'rb')
        )


orders = {}

def starts(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать!")

def receive_order(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    order = update.message.text
    orders[user_id] = order
    context.bot.send_message(chat_id=user_id, text="Спасибо за заказ!")

def display_orders(update: Update, context: CallbackContext):
    orders_text = ""
    for user_id, order in orders.items():
        orders_text += f"{user_id}: {order}\n"
    if orders_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=orders_text)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Пока нет заказов.")


def zakaz(update:Update,context: CallbackContext):
        text = update.message.text
        if text [:1] == 'Заказать':
                context.bot.send_message(
                        chat_id = '@gavno2123',
                        text = text
                )

def how_to_zakaz(update:Update, context: CallbackContext):
        update.message.reply_text(

                text="""
1.Напишите сообщение с большой буквы 'Заказ' 
2 ваше имя
3.Ваш номер.
4.Выберите куда вам доставить
5 И что вы выбрали, пример:Лагман, Манты
И позже с вами свяжутся           
                """
                  )
        

def contacti(update: Update, context: CallbackContext):
     update.message.reply_text(
          text='наши контакты: +996500557308, +996557557308 '
     )


# Add handlers to the dispatcher
# dispatcher = updater.dispatcher
# dispatcher.add_handler(CommandHandler('start', starts))
# dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_order))
# dispatcher.add_handler(CommandHandler('orders', display_orders))
 

MENU = menu[0]
ZAKAZ = menu[1]
LOCATION = menu[2]
CONTACTS = menu[3]
BACK = back

updater = Updater(token, persistence=PicklePersistence(filename='bot_data')) 
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MENU),
    menus
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.dispatcher.add_handler(MessageHandler(
   Filters.regex(CONTACTS),
    contacti
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    backo
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAKAZ),
    how_to_zakaz
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zakaz
))



dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', starts))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, receive_order))
dispatcher.add_handler(CommandHandler('orders', display_orders))

print(orders)
updater.start_polling() 
updater.idle()



