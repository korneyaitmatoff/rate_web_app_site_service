from pydantic import StrictInt

from api.api import Api
from config import VALIDATION_API_HOST, VALIDATION_API_PORT


class ValidationApi(Api):
    PATH = ''

    def __init__(self):
        super().__init__(host=VALIDATION_API_HOST, port=VALIDATION_API_PORT, path=self.PATH)

    def get_html_logs_by_site_id(self, site_id: int):
        """Получение списка html логов по id сайта

        Args:
            id: идентификатор сайта
        """
        return self.get(url=f"{self.url}/html_val/{site_id}").json()

    def get_css_logs_by_site_id(self, site_id: int):
        """Получение списка css логов по id сайта

        Args:
            id: идентификатор сайта
        """
        return self.get(url=f"{self.url}/css_val/{site_id}").json()

    def get_css_stat(self, site_id: int):
        return self.get(url=f"{self.url}/css_val/stat/{site_id}").json()

    def get_html_stat(self, site_id: int):
        return self.get(url=f"{self.url}/html_val/stat/{site_id}").json()