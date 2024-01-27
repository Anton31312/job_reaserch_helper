import os
from pprint import pprint
from typing import Dict, Optional, List
import requests
from dotenv import load_dotenv

from src.func import dict_to_instance
from src.abstract_parser import AbstractParser
from src.vacancy import Vacancy


load_dotenv() # Функция для загрузки переменных окружения


class SuperJobParser(AbstractParser):
    """
    Класс SuperJobParser наследуется от абстрактного класса AbstractParser. 
    Предназначен для запроса к API сервиса SuperJob и получению вакансий.
    """
    headers: Dict[str, str] = {'X-Api-App-Id': os.environ.get("SUPER_JOB_TOKEN")}
    base_url: str = 'https://api.superjob.ru/2.0/vacancies/'
    params = {"count": 100, "page": 0, "archive": False}

    def get_vacancy(self, keyword: Optional[str] = None) -> List[Vacancy]:
        """
        Функция get_vacancy переопределяет абстрактный метод базового класса. 

        Она содержит необходимые настройки и при вызове
        делает запрос API к сервису SuperJob, получает результат запроса,
        преобразует ответ и возвращает его.
        
        :Параметры:
        ---------
        keyword : str
                    Ключевое слово

        :Возвращаемое значение:
        ----------------------
        vacancies : list
                    Список экземпляров класса Vacancy
        """
        if keyword is not None:
            self.params["keyword"] = keyword
        response = requests.get(self.base_url, headers=self.headers, params=self.params).json()['objects']

        vacancies: list = list()

        for item in response:
            result: dict = {}
            result["name"] = item.get('profession')
            result["url"] = item.get('link')
            result["employer"] = item.get('client').get('title', 'Unknown')
            result["salary_from"] = item.get('payment_from', None)
            result["salary_to"] = item.get('payment_to', None)
            result["description"] = item.get('candidat', None)

            vacancies.append(result)

        return dict_to_instance(vacancies)

# Код для проверки корректности функционирования класса
if __name__ == '__main__':
    from views.view import display_vacancy

    sj = SuperJobParser()
    vac = sj.get_vacancy('Python')
    display_vacancy(vac)