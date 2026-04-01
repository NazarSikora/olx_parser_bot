from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привіт! Я бот для моніторингу цін на OLX.\n\n"
        "📌 Команди:\n"
        "/add <посилання> — додати оголошення\n"
        "/list — переглянути збережені оголошення\n"
        "/get — отримати актуальні ціни\n"
        "/delete <id> — видалити оголошення"
    )