from dataclasses import asdict
from typing import List, Dict, Any
import marshmallow
import marshmallow_dataclass

from src.vacancy import Vacancy


def dict_to_instance(data: List[Dict[str, Any]]) -> List[Vacancy]:
    """
    Функция dict_to_instance является вспомогательной функцией. 
    Выполняет проверку данных и создание экземпляров класса Vacancy. 
    Если получена ошибка проверки данных, создаваемый экземпляр пропускается.

    Параметры
    ---------
    data : List
            Список словарей с данными для создания экземпляров класса Vacancy. 

    :return: List экземпляров класса Vacancy.
    """
    result: list = []
    VacancySchema = marshmallow_dataclass.class_schema(Vacancy)

    for item in data:
        try:
            result.append(VacancySchema().load(item))
        except marshmallow.exceptions.ValidationError:
            continue
    return result


def instance_to_dict(data: List[Vacancy]) -> List[Dict[str, Any]]:
    """
    Функция instance_to_dict является вспомогательной функцией. 
    Производит создание словарей с данными.

    Параметры
    ---------
    data : List
            Список экземпляров класса Vacancy.

    :return: List словарей с данными.
    """
    result: list = []
    for item in data:
        result.append(asdict(item))
    return result


def create_dict_for_data_frame_pandas(data: List[Vacancy]) -> Dict[str, list]:
    """
    Функция create_dict_for_data_frame_pandas является вспомогательной функцией. 
    Создает словарь данных для создания объекта DataFrame из библиотеки pandas.
    
    Параметры
    ---------
    data : List
            Список экземпляров класса Vacancy. 
    
    :return: Dict с данными.
    """
    new_data: dict = {"name": [],
                       "url": [],
                       "employer": [],
                       "salary_from": [],
                       "salary_to": [],
                       "description": []}
    for item in data:
        new_data["name"].append(item.name)
        new_data["url"].append(item.url)
        new_data["employer"].append(item.employer)
        new_data["salary_from"].append(item.salary_from)
        new_data["salary_to"].append(item.salary_to)
        new_data["description"].append(item.description)

    return new_data