import httpx
import os

async def buscar_clima(cidade: str):
    key = os.getenv("OPENWEATHER_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": cidade, "appid": key, "units": "metric", "lang": "pt_br"}

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        if resp.status_code != 200:
            return None
        dados = resp.json()
        return {
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],
            "descricao": dados["weather"][0]["description"]
        }