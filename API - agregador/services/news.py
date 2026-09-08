import httpx
import os

async def buscar_noticias(cidade: str):
    key = os.getenv("NEWSAPI_KEY")
    url = "https://newsapi.org/v2/everything"
    params = {"q": cidade, "apiKey": key, "language": "pt", "pageSize": 5}

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        if resp.status_code != 200:
            return []
        dados = resp.json()
        return [
            {"titulo": a["title"], "fonte": a["source"]["name"], "url": a["url"]}
            for a in dados.get("articles", [])
        ]