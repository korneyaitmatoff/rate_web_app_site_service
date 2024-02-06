from pydantic import StrictInt

from api.api import Api
from config import VALIDATION_API_HOST, VALIDATION_API_PORT


class ValidationApi(Api):
    PATH = '/html_val'

    def __init__(self):
        super().__init__(host=VALIDATION_API_HOST, port=VALIDATION_API_PORT, path=self.PATH)

    def get_logs_by_site_id(self, id: StrictInt):
        """Получение списка логов по id сайта

        Args:
            id: идентификатор сайта
        """
        return self.get(url=f"{self.url}/{id}").json()
