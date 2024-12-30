import asyncio

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from src.text_processing.text_processor import TextProcessor
from src.analysis.analyzer import Analyzer


class LingoBot:
    def __init__(self, telegram_token: str):
        self.app = Application.builder().token(telegram_token).build()
        self.text_processor = TextProcessor()
        self.analyzer = Analyzer()
        self.setup_handlers()

    def setup_handlers(self):
        # Обработчики команд
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("tokenize", self.tokenize_command))
        self.app.add_handler(CommandHandler("stem", self.stem_command))
        self.app.add_handler(CommandHandler("lemmatize", self.lemmatize_command))
        self.app.add_handler(CommandHandler("analyze", self.analyze_command))
        self.app.add_handler(CommandHandler("sentiment", self.sentiment_command))
        self.app.add_handler(CommandHandler("stats", self.stats_command))
    
        # Обработчик текстовых сообщений
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_message_handler))
      
    async def start_command(self, update: Update):
        await update.message.reply_text("Привет! Я LingoBot. Используй /help, чтобы узнать, что я умею.")

    async def help_command(self, update: Update):
        help_text = """
        Я LingoBot - бот для лингвистического анализа текста.
        Доступные команды:
        /start - Начать
        /help - Помощь
        /tokenize - Токенизировать текст
        /stem - Стеммировать текст
        /lemmatize - Лемматизировать текст
        /analyze - Анализировать текст
        /sentiment - Определить тональность текста
        /stats - Получить статистику по тексту
        """
        await update.message.reply_text(help_text)
      
    async def text_message_handler(self, update: Update):
        text = update.message.text
        await update.message.reply_text(f"Вы отправили текст: {text}")

    async def tokenize_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            tokens = self.text_processor.tokenize(text, "line")
            output = "\n".join(tokens)
            await update.message.reply_text(f"Токенизированный текст:\n{output}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /tokenize")

    async def stem_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            stems = self.text_processor.stem(text, "line")
            output = "\n".join(stems)
            await update.message.reply_text(f"Стеммированный текст:\n{output}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /stem")
    
    async def lemmatize_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            lemmas = self.text_processor.lemmatize(text, "line")
            output = "\n".join(lemmas)
            await update.message.reply_text(f"Лемматизированный текст:\n{output}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /lemmatize")

    async def analyze_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            output = self.analyzer.analyze_text(text)
            await update.message.reply_text(f"Результаты анализа:\n{output}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /analyze")
    
    async def sentiment_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            sentiment = self.analyzer.analyze_sentiment(text)
            await update.message.reply_text(f"Тональность текста:\n{sentiment}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /sentiment")
        
    async def stats_command(self, update: Update, context: CallbackContext):
        if context.args:
            text = ' '.join(context.args)
            stats = self.analyzer.get_text_stats(text)
            await update.message.reply_text(f"Статистика текста:\n{stats}")
        else:
            await update.message.reply_text("Пожалуйста, введите текст после команды /stats")
    
    async def run(self):
        async with self.app:
            await self.app.initialize()
            task = asyncio.create_task(self.app.run_polling())
            try:
                await task
            finally:
                await self.app.shutdown()


async def main():
    telegram_token = "7995313293:AAHde8mwZmPROvJ_5xZppcZNLGuIs-3kOlg"
    bot = LingoBot(telegram_token)
    await bot.run()

if __name__ == '__main__':
    asyncio.run(main())
