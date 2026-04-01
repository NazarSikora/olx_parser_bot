from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.db import delete_listing

router = Router()


@router.message(Command("delete"))
async def cmd_delete(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer("❌ Вкажи ID оголошення. Приклад:\n/delete 3")
        return

    try:
        listing_id = int(parts[1].strip())
    except ValueError:
        await message.answer("❌ ID має бути числом. Приклад:\n/delete 3")
        return

    await delete_listing(listing_id=listing_id, user_id=message.from_user.id)

    await message.answer(f"🗑 Оголошення #{listing_id} видалено.")