import requests


class BaseApi(ABC):

    @abstractmethod
    def get_vacancy(self, keyword):
        pass


class HHApi(BaseApi):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}


    def get_vacancy(self, keyword):
        self.params.update({'text': keyword})
        response = requests.get(self.url,params=self.params)
        return response.json()['items']