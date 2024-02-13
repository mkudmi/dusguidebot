from telegram.ext import *

from ButtonHandlers import ButtonHandlers
from buttons.main_menu.MainMenuButtons import *
from messages.main_page import hello_message


class Bot:
    def __init__(self, token):
        self.token = token
        self.application = Application.builder().token(token).build()

        self.button_handlers = ButtonHandlers()

        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CallbackQueryHandler(self.button))
        self.application.add_handler(CommandHandler("help", self.help_command))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [InlineKeyboardButton("Интересные места", callback_data='2')],
            [InlineKeyboardButton("Магазины", callback_data='4')],
            [InlineKeyboardButton("Спорт", callback_data='3')],
            [InlineKeyboardButton("Транспорт", callback_data='6')],
            [InlineKeyboardButton("Полезности", callback_data='7')],
            [InlineKeyboardButton("О нас", callback_data='1'),
             InlineKeyboardButton("Предложка", callback_data='5')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message_text = hello_message
        image_url = 'pics/main_menu/mainpage.jpg'
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=message_text,
                                     reply_markup=reply_markup)

    async def button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        data = query.data

        handler = self.button_handlers.get_handler(data)
        if handler:
            await handler.handle(update, context)
        elif data == 'back':
            chat_id = query.message.chat_id
            message_id = query.message.message_id
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await self.start(update, context)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Используйте /start для отображения кнопок")

    def run(self):
        self.application.run_polling()

if __name__ == '__main__':
    bot_token = "6951169119:AAH7q8B_YRa_sRk3nveqTzyIQVzb1bIqQMk"
    bot = Bot(bot_token)
    bot.run()
