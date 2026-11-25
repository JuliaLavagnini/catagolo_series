from pydantic import BaseModel, Field


class CreateSeries(BaseModel):
    title: str = Field(..., min_length=1, description="Series title")
    genre: str = Field(..., min_length=1, description="Series genre")
    release_year: int = Field(
        ..., gt=1900, description="Release year (greater than 1900)"
    )
    seasons: int = Field(..., gt=0, description="Number of seasons of the series")


class SeriesResponse(BaseModel):
    message: str
    series: CreateSeries
