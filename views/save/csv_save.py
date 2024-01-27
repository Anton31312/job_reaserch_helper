import csv
from typing import List, Dict, Any

from src.func import instance_to_dict, dict_to_instance
from src.vacancy import Vacancy
from views.save.abstract_save import AbstractSave


class CSVSave(AbstractSave):
    """
    Класс CSVSave предназначен для предоставления отчета-файла в формате CSV.
    Унаследован от абстрактного базового класса AbstractSave.
    """
    file_path: str = 'save_files/csv_vacancy_data.csv'

    def write_data(self, data: List[Vacancy]) -> None:
        """
        Функция write_data переопределяет абстрактный метод базового класса.
        Преобразует переданные данные в список словарей и записывает данные в csv-файл,
        путь к которому указан в аргументах класса. 

        Параметры
        ---------
        data : List
                Список экземпляров класса Vacancy.
    
        """
        data.sort(key=lambda x: x.salary_from, reverse=True)
        vacancies: List[Dict[str, Any]] = instance_to_dict(data)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=vacancies[0])
            writer.writeheader()
            writer.writerows(vacancies)


    def get_data(self) -> List[Vacancy]:
        """
        Функция get_data переопределяет абстрактный метод базового класса.
        Он считывает все данные из CSV-файла, путь к которому определен
        в аргументах класса, и преобразует полученные данные в список экземпляров класса Vacancy.
        
        Функция принимает в качестве параметра экземпляр собственного класса. 
        
        :return: List.
        """
        with open(self.file_path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            vacancies: List[Dict[str, Any]] = []
            for row in reader:
                vacancies.append(row)
        return dict_to_instance(vacancies)


# Код для проверки корректности функционирования класса
if __name__ == '__main__':
    from src.hhru.hhru_parser import HHruParser
    from views.view import display_vacancy

    hh = HHruParser()
    data = hh.get_vacancy('Python разработчик')

    save = CSVSave()

    save.write_data(data)
    display_vacancy(save.get_data())
    vac = Vacancy(name="test", url="test", employer="test", salary_from=0, salary_to=None, description=None)
    #save.add_vacancy(vac)
    # display_vacancy(save.get_data())
    #save.delete_vacancy(vac)
    # display_vacancy(save.get_data())
    # display_vacancy(save.get_vacancies_by_salary("150 000-200 000 руб."))
    #save.delete_data()