from enum import StrEnum
from typing import Optional
from typing_extensions import TypedDict

from pydantic import BaseModel


class EnumCategories(StrEnum):
    """Перечисление списка категорий сайтов"""
    blog = "blog"
    shop = "shop"
    social_net = "social_net"
    other = "other"


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
