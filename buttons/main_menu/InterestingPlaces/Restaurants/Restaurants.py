from telegram import *
from telegram.ext import ContextTypes

from messages.restaurants import jenka_info


class JenkaButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/aboutus.jpg'
        text = jenka_info

        keyboard = [
            [InlineKeyboardButton("Сайт", url='https://jenka-restaurant-bar.eatbu.com/?lang=en'),
             InlineKeyboardButton("На карте", url='https://maps.app.goo.gl/kZbkgJNkzMAMs3q67'),
             InlineKeyboardButton("Меню", url='https://cdn.website.dish.co/media/dd/60/7608050/Speisekarte.pdf')],
            [InlineKeyboardButton("Назад", callback_data='back_to_restaurants')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)