from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from services.climate import buscar_clima
from services.news import buscar_noticias
import asyncio

load_dotenv()
app = FastAPI(title="Agregador de Cidade")

@app.get("/resumo/{cidade}")
async def resumo_cidade(cidade: str):
    climate, news = await asyncio.gather(
        buscar_clima(cidade),
        buscar_noticias(cidade)
    )

    if climate is None:
        raise HTTPException(status_code=404, detail="Cidade não encontrada no serviço de clima")

    return {
        "cidade": cidade,
        "clima": climate,
        "noticias": news
    }