from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.db import get_listings

router = Router()


@router.message(Command("list"))
async def cmd_list(message: Message):
    listings = await get_listings(user_id=message.from_user.id)

    if not listings:
        await message.answer("📭 У тебе поки немає збережених оголошень.\n\nДодай через /add <посилання>")
        return

    text = "📋 Твої оголошення:\n\n"

    for listing in listings:
        listing_id, url, title, price = listing
        text += (
            f"🔹 ID: {listing_id}\n"
            f"📦 {title}\n"
            f"💰 {price}\n"
            f"🔗 {url}\n\n"
        )

    await message.answer(text)