import aiosqlite

DB_PATH = "listings.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                url TEXT NOT NULL,
                title TEXT NOT NULL,
                price TEXT NOT NULL
            )
        """)
        await db.commit()


async def add_listing(user_id: int, url: str, title: str, price: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO listings (user_id, url, title, price) VALUES (?, ?, ?, ?)",
            (user_id, url, title, price)
        )
        await db.commit()


async def get_listings(user_id: int) -> list:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT id, url, title, price FROM listings WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            return await cursor.fetchall()


async def delete_listing(listing_id: int, user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "DELETE FROM listings WHERE id = ? AND user_id = ?",
            (listing_id, user_id)
        )
        await db.commit()


async def update_price(listing_id: int, new_price: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE listings SET price = ? WHERE id = ?",
            (new_price, listing_id)
        )
        await db.commit()