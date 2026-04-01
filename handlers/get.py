from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database.db import get_listings, update_price
from parser.olx import parse_olx_listing

router = Router()


@router.message(Command("get"))
async def cmd_get(message: Message):
    listings = await get_listings(user_id=message.from_user.id)

    if not listings:
        await message.answer("📭 У тебе поки немає збережених оголошень.\n\nДодай через /add <посилання>")
        return

    await message.answer("⏳ Перевіряю ціни...")

    for listing in listings:
        listing_id, url, title, old_price = listing

        data = await parse_olx_listing(url)

        if data is None:
            await message.answer(
                f"⚠️ Не вдалось отримати дані\n"
                f"📦 {title}\n"
                f"🔗 {url}"
            )
            continue

        new_price = data["price"]

        if new_price != old_price:
            await update_price(listing_id, new_price)
            await message.answer(
                f"🔄 Ціна змінилась!\n\n"
                f"📦 {title}\n"
                f"📉 Було: {old_price}\n"
                f"📈 Стало: {new_price}\n"
                f"🔗 {url}"
            )
        else:
            await message.answer(
                f"✅ Ціна не змінилась\n\n"
                f"📦 {title}\n"
                f"💰 {new_price}\n"
                f"🔗 {url}"
            )