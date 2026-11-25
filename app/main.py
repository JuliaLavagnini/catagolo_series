'''Entry point and FastAPI app setup'''

from fastapi import FastAPI
from app.routes import router as series_rota

app = FastAPI(title="Catálogo de Séries API")

@app.get("/")
def home():
    return {"mensagem": "Catálogo de Séries em construção"}

app.include_router(series_rota)