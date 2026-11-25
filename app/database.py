import sqlite3
from fastapi import HTTPException, status

DB_PATH = "series.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    # Permite acessar as colunas pelo nome (row['titulo']) em vez de indice
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano_lancamento INTEGER NOT NULL,
                temporadas INTEGER NOT NULL
            )
        """)


def inserir_serie(serie: dict) -> dict:
    try:
        with get_connection() as conn:
            conn.execute(
                """
                        INSERT INTO series (titulo, genero, ano_lancamento, temporadas)
                        VALUES (?, ?, ?, ?)
                    """,
                (
                    serie["titulo"],
                    serie["genero"],
                    serie["ano_lancamento"],
                    serie["temporadas"],
                ),
            )
            return {"mensagem": "Série inserida com sucesso!", "serie": serie}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ja existe uma série com o título - {serie['titulo']}",
        )

def listar_series() -> list[dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM series")
        return [dict(row) for row in cursor.fetchall()]

def buscar_por_titulo(titulo: str) -> dict | None:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM series WHERE LOWER(titulo) = LOWER(?)", (titulo,))
        row = cursor.fetchone()
        return dict(row) if row else None