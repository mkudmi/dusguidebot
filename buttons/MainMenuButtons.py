from telegram import *
from telegram.ext import ContextTypes

from messages.main_page import about_us_message, proposal_message, info_sport


class AboutUsButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        # Удаление предыдущего сообщения
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/aboutus.jpg'
        text = about_us_message
        keyboard = [
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)


class InterestingPlacesButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/places.jpg'
        text = "Интересные места s"
        keyboard = [
            [InlineKeyboardButton("Парки", callback_data='parks')],
            [InlineKeyboardButton("Музеи", callback_data='museums')],
            [InlineKeyboardButton("Рестораны", callback_data='restaurants')],
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)

class SportsButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/sports.jpg'
        text_to_send = info_sport
        keyboard = [
            [InlineKeyboardButton("Секции", callback_data='sections')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text_to_send,
                                     reply_markup=reply_markup)


class SuggestionButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/proposal.jpg'
        text_to_send = proposal_message
        keyboard = [
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text_to_send,
                                     reply_markup=reply_markup)


class ShopsButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/shops.jpg'
        text_to_send = 'Информация о магазинах'
        keyboard = [
            [InlineKeyboardButton("Книги", callback_data='4-1')],
            [InlineKeyboardButton("Продукты", callback_data='4-2')],
            [InlineKeyboardButton("Спорт", callback_data='4-3')],
            [InlineKeyboardButton("Карнавал!", callback_data='4-4')],
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text_to_send,
                                     reply_markup=reply_markup)

class TransportButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/transport.jpg'
        text_to_send = 'Транспорт'
        keyboard = [
            [InlineKeyboardButton("49 Euro Ticket", callback_data='5-1')],
            [InlineKeyboardButton("Приложения", callback_data='5-2')],
            [InlineKeyboardButton("Билеты", callback_data='5-3')],
            [InlineKeyboardButton("За границу с проездным", callback_data='5-4')],
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text_to_send,
                                     reply_markup=reply_markup)

class StoriesButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/main_menu/utilities.jpg'
        text_to_send = 'Истории'
        keyboard = [
            [InlineKeyboardButton("Потеряли ключи от дома", callback_data='lost_keys')],
            [InlineKeyboardButton("Назад", callback_data='back')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text_to_send,
                                     reply_markup=reply_markup)