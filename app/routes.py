from typing import List
from fastapi import APIRouter, status, HTTPException
from app.schemas import CreateSeries, SeriesResponse
from app.database import (
    find_by_title,
    insert_series,
    list_all_series,
    delete_series_by_title,
)

router = APIRouter(prefix="/series", tags=["Series"])


# GET /series route to list the full catalogue
@router.get("", response_model=list[CreateSeries], status_code=status.HTTP_200_OK)
def list_series():
    return list_all_series()


# POST /series route
@router.post("", response_model=SeriesResponse, status_code=status.HTTP_201_CREATED)
def register_series(new_series: CreateSeries):
    return insert_series(new_series.model_dump())


@router.get("/{title}", response_model=CreateSeries, status_code=status.HTTP_200_OK)
def get_series(title: str):
    # Exact search
    series = find_by_title(title)

    # If not found and the URL has hyphens, try replacing them with spaces
    if not series and "-" in title:
        series = find_by_title(title.replace("-", " "))

    if not series:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Series not found"
        )
    return series


@router.delete("/{title}", status_code=status.HTTP_200_OK)
def delete_series(title: str):
    removed = delete_series_by_title(title)

    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Series not found"
        )
    return {"message": "Series '{title}' removed successfully!"}
