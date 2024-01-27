from typing import List
import pandas

from src.func import dict_to_instance, create_dict_for_data_frame_pandas
from src.vacancy import Vacancy
from views.save.abstract_save import AbstractSave


class ExcelSave(AbstractSave):
    """
    Класс ExcelSave предназначен для предоставления приложению файла в формате Excel.
    Унаследован от абстрактного базового класса AbstractSave.
    """
    file_path: str = './save_files/excel_vacancy_data.xlsx'

    def write_data(self, data: List[Vacancy]) -> None:
        """
        Функция write_data переопределяет абстрактный метод базового класса.
        Преобразует переданные данные в объект pandas DataFrame и записывает данные в файл Excel,
        путь к которому указан в аргументах класса. 
           
        Параметры
        ---------
        data : List
                Список экземпляров класса Vacancy.
        
        """
        data.sort(key=lambda x: x.salary_from, reverse=True)
        data_frame = pandas.DataFrame(create_dict_for_data_frame_pandas(data))
        data_frame.to_excel(self.file_path, index=False)

    def get_data(self) -> List[Vacancy]:
        """
        Функция get_data переопределяет абстрактный метод базового класса. 
        Он считывает все данные из файла Excel, путь к которому определен
        в аргументах класса, и преобразует полученные данные в список экземпляров класса Vacancy.

        Функция принимает в качестве параметра экземпляр собственного класса. 
        
        :return: List.
        """
        excel_data_frame = pandas.read_excel(self.file_path, sheet_name='Sheet1')
        return dict_to_instance(excel_data_frame.to_dict(orient='records'))


# Код для проверки корректности функционирования класса
if __name__ == '__main__':
    from src.hhru.hhru_parser import HHruParser

    hh = HHruParser()
    data = hh.get_vacancy()

    save = ExcelSave()
    save.write_data(data)
    save.delete_data()