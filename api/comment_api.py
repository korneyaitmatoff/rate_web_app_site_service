from pydantic import StrictInt

from api.api import Api
from config import COMMENT_API_HOST, COMMENT_API_PORT


class CommentApi(Api):
    PATH = '/comment'

    def __init__(self):
        super().__init__(host=COMMENT_API_HOST, port=COMMENT_API_PORT, path=self.PATH)

    def get_comments_by_site_id(self, id: StrictInt):
        """Получение списка комментариев по id сайта

        Args:
            id: идентификатор сайта
        """
        return self.get(url=f"{self.url}/{id}").json()
