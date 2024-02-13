from telegram import *
from telegram.ext import ContextTypes


class BadmintonButton:
    async def handle(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        chat_id = query.message.chat_id
        message_id = query.message.message_id

        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

        photo_url = 'pics/interesting_places/parks.jpg'
        text = 'инфо о бадминтоне'

        keyboard = [
            [InlineKeyboardButton("Назад", callback_data='back_to_sections')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=chat_id, photo=photo_url, caption=text, reply_markup=reply_markup)