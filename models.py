from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str
    author: str
    genre: str
    release_year: int = Field(..., alias="release_date")
    description: str
    cover: Optional[str] = None

    @classmethod
    def validate_year(cls, v):
        if not (1000 <= v <= 9999):
            raise ValueError("release_year must be a valid year")
        return v

    @property
    def release_date(self) -> date:
        return date(self.release_year, 1, 1)


