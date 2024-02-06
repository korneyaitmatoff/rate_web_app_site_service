from pydantic import StrictInt

from api.api import Api
from config import USER_API_HOST, USER_API_PORT


class UserApi(Api):
    PATH = '/user'

    def __init__(self):
        super().__init__(host=USER_API_HOST, port=USER_API_PORT, path=self.PATH)

    def get_user_by_id(self, id: StrictInt):
        return self.get(url=f"{self.url}/{id}").json()
