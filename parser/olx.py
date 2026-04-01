import httpx
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


async def parse_olx_listing(url: str) -> dict | None:
    try:
        async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
            response = await client.get(url, timeout=10)

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h4", class_="css-1kc83jo")
        price_tag = soup.find("div", class_="css-tr1x2n")

        if not title_tag or not price_tag:
            return None

        title = title_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True)

        return {"title": title, "price": price}

    except httpx.RequestError:
        return None