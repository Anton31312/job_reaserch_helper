from typing import List, Dict, Any, Optional
import requests

from src.func import dict_to_instance
from src.abstract_parser import AbstractParser
from src.vacancy import Vacancy


class HHruParser(AbstractParser):
    """
    Класс HHruParser наследуется от абстрактного класса AbstractParser. 
    Предназначен для запроса к API сервиса HeadHunter и получению вакансий.
    """
    base_url: str = 'https://api.hh.ru/vacancies'
    headers: Dict[str, str] = {"User_Agent": "user_agent"}
    params: Dict[str, Any] = {"archived": False, 'area': 113, 'per_page': 100}

    def get_vacancy(self, keyword: Optional[str] = None) -> List[Vacancy]:
        """
        Функция get_vacancy переопределяет абстрактный метод базового класса. 

        Она содержит необходимые настройки и при вызове
        делает запрос API к сервису HeadHunter, получает результат запроса,
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
            self.params["text"] = keyword

        response = requests.get(self.base_url, headers=self.headers, params=self.params).json()['items']

        vacancies: list = []

        for item in response:
            result: dict = {}
            result["name"] = item.get('name')
            result["url"] = item.get('alternate_url')
            result["employer"] = item.get('employer').get('name')
            if item["salary"] is not None:
                result["salary_from"] = item['salary'].get('from') if item['salary'].get('from') is not None else 0
                result["salary_to"] = item['salary'].get('to')if item['salary'].get('to') is not None else 0
            else:
                result["salary_from"] = 0
                result["salary_to"] = 0
            result["description"] = item["snippet"].get('requirement', None)

            vacancies.append(result)

        return dict_to_instance(vacancies)


# Код для проверки корректности функционирования класса
if __name__ == '__main__':
    from views.view import display_vacancy

    hh = HHruParser()
    vac = hh.get_vacancy('Разработчик Python')
    display_vacancy(vac)