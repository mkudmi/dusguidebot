from telegram import *
from telegram.ext import ContextTypes

from messages.sport import info_sections


class SectionsButton:

    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/sport/sections.jpg'
        text = info_sections

        keyboard = [
            [InlineKeyboardButton("Бадминтон", callback_data='badminton')],
            [InlineKeyboardButton("Пляжный волейбол", callback_data='beach_volleyball')],
            [InlineKeyboardButton("Назад", callback_data='back_to_sport')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)