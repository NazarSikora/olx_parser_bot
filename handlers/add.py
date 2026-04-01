from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from parser.olx import parse_olx_listing
from database.db import add_listing

router = Router()


@router.message(Command("add"))
async def cmd_add(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer("❌ Вкажи посилання. Приклад:\n/add https://www.olx.ua/...")
        return

    url = parts[1].strip()

    if "olx.ua" not in url:
        await message.answer("❌ Надішли посилання з сайту olx.ua")
        return

    await message.answer("⏳ Завантажую оголошення...")

    data = await parse_olx_listing(url)

    if data is None:
        await message.answer("❌ Не вдалось отримати дані. Перевір посилання.")
        return

    await add_listing(
        user_id=message.from_user.id,
        url=url,
        title=data["title"],
        price=data["price"]
    )

    await message.answer(
        f"✅ Збережено!\n\n"
        f"📦 {data['title']}\n"
        f"💰 {data['price']}"
    )