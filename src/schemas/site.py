from typing import Optional
from typing_extensions import TypedDict

from pydantic import BaseModel

from src.database.tables import EnumCategories


class Site(BaseModel):
    """Модель сайта"""
    id: int
    name: str
    description: Optional[str]
    url: str
    user_id: int
    category: EnumCategories


class SiteDict(TypedDict):
    """Словарь принимаемых аргументов"""
    name: str
    description: Optional[str]
    url: str
    user_id: int
    category: EnumCategories
