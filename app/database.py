import sqlite3
from fastapi import HTTPException, status

DB_PATH = "series.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    # Allows accessing columns by name (row['title']) instead of index
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                seasons INTEGER NOT NULL
            )
        """)


def insert_series(series: dict) -> dict:
    try:
        with get_connection() as conn:
            conn.execute(
                """
                        INSERT INTO series (title, genre, release_year, seasons)
                        VALUES (?, ?, ?, ?)
                    """,
                (
                    series["title"],
                    series["genre"],
                    series["release_year"],
                    series["seasons"],
                ),
            )
            return {"message": "Series inserted successfully!", "series": series}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"A series with this title already exists - {series['title']}",
        )


def list_all_series() -> list[dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM series")
        return [dict(row) for row in cursor.fetchall()]


def find_by_title(title: str) -> dict | None:
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT * FROM series WHERE LOWER(title) = LOWER(?)", (title,)
        )
        row = cursor.fetchone()
        return dict(row) if row else None


def delete_series_by_title(title: str) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM series WHERE LOWER(title) = LOWER(?)", (title,)
        )
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Series not found"
            )
        return cursor.rowcount > 0
