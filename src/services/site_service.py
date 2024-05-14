from fastapi.exceptions import HTTPException

from api.user_api import UserApi
from api.comment_api import CommentApi
from api.validation_api import ValidationApi
from src.services.service import Service
from src.schemas.site import SiteDict, Site, EnumCategories
from src.repositories.repository import Repository


class SiteService(Service):
    """Класс-сервис для работы с сущностью "Сайт" """

    def __init__(self, repository: Repository):
        super().__init__(repository=repository)

    def get_sites(self, limit: int = 10000, offset: int = 0):
        return self.read(limit=limit, offset=offset)

    def get_site_by_id(self, site_id: int) -> Site:
        data = self.read(filters=(self.repository.table.id == site_id,))

        if data:
            return data[0]
        else:
            raise HTTPException(404, "site not found")

    def get_sites_by_user_id(self, user_id: int) -> list[Site]:
        return self.read(filters=(self.repository.table.user_id == user_id,))

    def edit_site(self, site_id: int, site: SiteDict):
        self.repository.update(id=site_id, data=dict(site))

        return site_id

    def create_site(self, site: SiteDict) -> Site:
        return self.create(site)

    def delete_site(self, site_id: int):
        self.delete(filters=(self.repository.table.id == site_id,))

    def get_site_data(self, site_id: int):
        """Получение всех данных сайта

        Args:
            site_id: идентификатор сайта
        """
        data = self.get_site_by_id(site_id=site_id)

        user = UserApi().get_user_by_id(id=data.user_id)
        comments = CommentApi().get_comments_by_site_id(id=data.id)

        return {
            "user": user,
            "data": data,
            "comments": comments,
            "validation": {
                "html":  ValidationApi().get_html_logs_by_site_id(site_id=data.id),
                "css":  ValidationApi().get_css_logs_by_site_id(site_id=data.id)
            }
        }

    def get_sites_by_category(self, category: EnumCategories):
        return self.repository.read(filters=(self.repository.table.category == category,))

    def get_site_stat(self, site_id: int):
        return {
            "html": ValidationApi().get_html_stat(site_id=site_id),
            "css": ValidationApi().get_css_stat(site_id=site_id),
        }
