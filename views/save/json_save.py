import json
from typing import List, Dict, Any

from src.func import instance_to_dict, dict_to_instance
from src.vacancy import Vacancy
from views.save.abstract_save import AbstractSave


class JsonSave(AbstractSave):
    """
    Класс JsonSave предназначен для предоставления приложению файла в формате JSON.
    Унаследован от абстрактного базового класса AbstractSave.
    """
    file_path: str = './save_files/json_vacancy_data.json'

    def write_data(self, data: List[Vacancy]) -> None:
        """
        Функция write_data переопределяет абстрактный метод базового класса. 
        Преобразует переданные данные в список словарей и записывает данные в файл JSON,
        путь к которому указан в аргументах класса.

        Параметры
        ---------
        data : List
                Список экземпляров класса Vacancy.
 
        """
        data.sort(key=lambda x: x.salary_from, reverse=True)
        vacancies: List[Dict[str, Any]] = instance_to_dict(data)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)

    def get_data(self) -> List[Vacancy]:
        """
        Функция get_data переопределяет абстрактный метод базового класса. 
        Он считывает все данные из файла JSON, путь к которому определен
        в аргументах класса, и преобразует полученные данные в список экземпляров класса Vacancy.
        
        Функция принимает в качестве параметра экземпляр собственного класса.

        :return: List.
        """
        with open(self.file_path, encoding="utf8") as file:
            vacancies: List[Dict[str, Any]] = json.load(file)
        return dict_to_instance(vacancies)


# Код для проверки корректности функционирования класса
if __name__ == '__main__':
    from src.hhru.hhru_parser import HHruParser
    from views.view import display_vacancy

    hh = HHruParser()
    data = hh.get_vacancy('python')

    save = JsonSave()

    save.write_data(data)
    display_vacancy(save.get_data())
    vac = Vacancy(name="test", url="test", employer="test", salary_from=0, salary_to=None, description=None)
    save.add_vacancy(vac)
    # display_vacancy(save.get_data())
    save.delete_vacancy(vac)
    # display_vacancy(save.get_data())
    display_vacancy(save.get_vacancies_by_salary("150 000-200 000 руб."))
    save.delete_data()