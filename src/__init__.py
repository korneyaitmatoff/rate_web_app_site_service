from typing import List

from fastapi import FastAPI

from src.app import App
from src.database import tables
from src.repositories import SiteRepository
from src.services.site_service import SiteService
from src.schemas.site import Site
from src.routes.site import SiteRouter

server = (app := App(server=FastAPI())).get_app()

# Сервисы
site_service = SiteService(repository=SiteRepository(table=tables.Site, database_handler=app.db_handler))

# Роутеры
app.register_routes([
    SiteRouter(
        service=site_service,
        routes=[
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": List[Site],
                "description": "Получение списка сайтов", "methods": ['GET'],
                "endpoint": site_service.get_sites
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Получение сайта по id", "methods": ['GET'],
                "endpoint": site_service.get_site_by_id
            },
            {
                "path": "",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Создание сайта", "methods": ['POST'],
                "endpoint": site_service.create_site
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Удаление сайта", "methods": ['PUT'],
                "endpoint": site_service.delete_site
            },
            {
                "path": "/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": Site,
                "description": "Изменение данных сайта", "methods": ['PATCH'],
                "endpoint": site_service.edit_site
            },
            {
                "path": "/user/{user_id}",
                "responses": {400: {"description": "Bad request"}},
                "response_model": list[Site],
                "description": "Получение списка сайтов по id пользователя", "methods": ['GET'],
                "endpoint": site_service.get_sites_by_user_id
            },
            {
                "path": "/data/{site_id}",
                "responses": {400: {"description": "Bad request"}},
                "description": "Всех данных сайта", "methods": ['GET'],
                "endpoint": site_service.get_site_data
            },
        ]
    ).get_router()
])
