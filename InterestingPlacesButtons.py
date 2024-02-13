from telegram import *
from telegram.ext import ContextTypes

from messages.parks import info_parks
from messages.restaurants import rest_info


class ParksButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/interesting_places/parks.jpg'
        text = info_parks

        keyboard = [
            [InlineKeyboardButton("Назад", callback_data='back_to_interesting_places')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)

class MuseumsButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/aboutus.jpg'
        text = "Музеи"

        keyboard = [
            [InlineKeyboardButton("Назад", callback_data='back_to_interesting_places')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)

class RestaurantsButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/aboutus.jpg'
        text = 'Рестораны'

        keyboard = [
            [InlineKeyboardButton("Jenka (Украинско-Русская кухня)", callback_data='jenka')],
            [InlineKeyboardButton("Назад", callback_data='back_to_interesting_places')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)