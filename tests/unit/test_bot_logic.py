import pytest
from unittest.mock import AsyncMock
from src.bot.bot import LingoBot
from telegram import Update, Message
from telegram.ext import CallbackContext


@pytest.fixture
def bot():
    return LingoBot("test_token")


@pytest.mark.asyncio
async def test_start_command(bot):
    update_mock = AsyncMock(spec=Update)
    message_mock = AsyncMock(spec=Message)
    context_mock = AsyncMock(spec=CallbackContext)
    update_mock.message = message_mock

    await bot.start_command(update_mock, context_mock)

    message_mock.reply_text.assert_called_once()


@pytest.mark.asyncio
async def test_help_command(bot):
    update_mock = AsyncMock(spec=Update)
    message_mock = AsyncMock(spec=Message)
    context_mock = AsyncMock(spec=CallbackContext)
    update_mock.message = message_mock

    await bot.help_command(update_mock, context_mock)

    message_mock.reply_text.assert_called_once()


@pytest.mark.asyncio
async def test_text_message_handler(bot):
    update_mock = AsyncMock(spec=Update)
    message_mock = AsyncMock(spec=Message)
    context_mock = AsyncMock(spec=CallbackContext)
    update_mock.message = message_mock
    message_mock.text = "test message"

    await bot.text_message_handler(update_mock, context_mock)
    message_mock.reply_text.assert_called_once_with("Вы отправили текст: test message")
