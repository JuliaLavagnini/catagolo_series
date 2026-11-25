from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.routes import router as series_router
from app.database import init_db

init_db()

app = FastAPI(title="Series Catalogue API")

# Allows access for the front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


app.include_router(series_router)
